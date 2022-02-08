package service.broker;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.lang.Thread;

import javax.jms.Connection;
import javax.jms.ConnectionFactory;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.MessageProducer;
import javax.jms.Queue;
import javax.jms.Session;
import javax.jms.Topic;
import javax.jms.ObjectMessage;

import org.apache.activemq.ActiveMQConnectionFactory;

import service.core.ClientInfo;
import service.core.Quotation;
import service.message.QuotationRequestMessage;
import service.message.QuotationResponseMessage;
import service.message.ClientApplicationMessage;

/**
 * Implementation of the broker service that uses the Service Registry.
 * 
 * @author Rem
 *
 */
public class Broker  {
	static Map<Long, ClientInfo> cache = new HashMap<Long,ClientInfo>();
	private static Connection connection;
    public static void main(String[] args) {
        String host = args.length == 0 ? "localhost":args[0];
		try{
			ConnectionFactory factory = 
					new ActiveMQConnectionFactory("failover://tcp://"+host+":61616"); 
			connection = factory.createConnection(); 
			connection.setClientID("broker"); 
			CbsThread cbsThread = new CbsThread();
			SbcThread sbcThread = new SbcThread();
			new Thread(cbsThread).start();
			new Thread(sbcThread).start();
		}catch (JMSException e){
			System.out.println(e);
		}
	}


public static class CbsThread implements Runnable{
	@Override
	public void run () {
		try{

			Session session = connection.createSession(false, Session.CLIENT_ACKNOWLEDGE); 
			Queue requests = session.createQueue("REQUESTS");	
			Queue queue = session.createQueue("QUOTATIONS"); 
			Topic topic = session.createTopic("APPLICATIONS"); 
			MessageProducer producer = session.createProducer(topic); 
			MessageConsumer consumer = session.createConsumer(queue); 

			connection.start();
			
			while (true) {
				Message message = consumer.receive(); 
				if (message instanceof ObjectMessage) { 
						Object content = ((ObjectMessage) message).getObject(); 
						if (content instanceof QuotationResponseMessage) { 
							QuotationResponseMessage request = (QuotationResponseMessage) content; 
							producer.send(message);
							cache.put(request.id,request.info);
						} 
						
				} else { 
						System.out.println("Unknown message type: " + 
								message.getClass().getCanonicalName()); 
				} 
			}
		}catch (JMSException e) {
			System.out.println(e);
		}
	}

}

public static class SbcThread implements Runnable{

	@Override
	public void run(){
		try{
			Session session = connection.createSession(false, Session.CLIENT_ACKNOWLEDGE); 
				
			Queue queue = session.createQueue("QUOTATIONS"); 
			Topic topic = session.createTopic("APPLICATIONS"); 
			MessageProducer producer = session.createProducer(topic); 
			MessageConsumer consumer = session.createConsumer(queue); 
			MessageConsumer consumer2 = session.createConsumer(queue);
			connection.start();

			while (true) {
				
                ArrayList<Quotation> quotations = new ArrayList<>();
                
				Message message = consumer.receive(); 
				if (message instanceof ObjectMessage) { 
						Object content = ((ObjectMessage) message).getObject(); 
						if (content instanceof QuotationRequestMessage) { 
							QuotationRequestMessage request = (QuotationRequestMessage) content; 
							System.out.println(request.id); 
						}
					} else {
						System.out.println("Unknown message type: " +
								message.getClass().getCanonicalName());
					}
			
			System.out.println(quotations);
			
			
			}

	} catch (JMSException e){
		System.out.println(e);
		
	}
	
	}
	
	}

}



