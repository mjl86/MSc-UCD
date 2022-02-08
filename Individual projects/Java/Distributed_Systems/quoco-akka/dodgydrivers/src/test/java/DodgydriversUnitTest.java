import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;


import akka.actor.ActorRef;
import akka.actor.Props;
import akka.actor.ActorSystem;
import akka.testkit.javadsl.TestKit;
import service.actor.Quoter;
import service.dodgydrivers.DDQService;
import service.core.ClientInfo;
import service.message.Init;
import service.messages.QuotationRequest;
import service.messages.QuotationResponse;;
public class DodgydriversUnitTest {

    static ActorSystem system;

    @BeforeClass
     public static void setup() {
         system = ActorSystem.create();
     }
 
     @Test 
 public void testQuoter() { 
     ActorRef quoterRef = system.actorOf(Props.create(Quoter.class), "test");
     TestKit probe = new TestKit(system);
     
     quoterRef.tell(new Init(new DDQService()), null); 
     quoterRef.tell(new QuotationRequest(1, 
         new ClientInfo("Niki Collier", ClientInfo.getFEMALE(), 43, 0, 5, "PQR254/1")), 
         probe.getRef()); 
     probe.awaitCond(probe::msgAvailable); 
     probe.expectMsgClass(QuotationResponse.class); 
     } 
    
}
