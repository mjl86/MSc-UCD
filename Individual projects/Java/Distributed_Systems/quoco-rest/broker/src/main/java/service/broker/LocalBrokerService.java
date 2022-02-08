package service.broker;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.http.HttpEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import service.core.ClientApplication;
import service.core.ClientInfo;
import service.core.Quotation;


/**
 * Implementation of the broker service that uses the Service Registry.
 * 
 * @author Rem
 *
 */
@RestController
public class LocalBrokerService  {

	
	static String[] services = {
		"http://localhost:8081/quotations",
		"http://localhost:8082/quotations",
		"http://localhost:8083/quotations"};

	int applicationNo;

	Map<Integer, ClientApplication> client_Application = new HashMap<>();

	@RequestMapping(value="/applications",method=RequestMethod.POST)
	public ClientApplication getApplication(@RequestBody ClientInfo info){
		ClientApplication clientApplication = new ClientApplication();
		System.out.println(info);

		clientApplication.setQuotationList((ArrayList<Quotation>) getQuotations(info));
		clientApplication.setClientInfo(info);
		clientApplication.setApplicationNo(applicationNo);

		client_Application.put(applicationNo++,clientApplication);

		return clientApplication;
	}


	public List<Quotation> getQuotations(ClientInfo info) {
		ArrayList<Quotation> quotations = new ArrayList<Quotation>();
		
		RestTemplate restTemplate = new RestTemplate();
		HttpEntity<ClientInfo> request = new HttpEntity<>(info);
		for (String service : services) {
			try{ Quotation quotation = restTemplate.postForObject(service, request, Quotation.class);
					quotations.add(quotation);
			}catch (Exception e){
				System.out.println(e);
				
			}
		}
		return quotations;
	}

	@RequestMapping(value="/applications/{application-number}",method= RequestMethod.GET)
	public ClientApplication searchApplication(@PathVariable("application-number") int parameter){
		return client_Application.get(parameter);
	}

	@RequestMapping(value="/applications",method= RequestMethod.GET)
	public ArrayList<ClientApplication> listApplication(){
		ArrayList<ClientApplication> list = new ArrayList<ClientApplication>(client_Application.values());
		return list;
	}

}
