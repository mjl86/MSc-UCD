package service.actor;


import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

import akka.actor.AbstractActor;
import akka.actor.ActorRef;

import service.messages.ApplicationRequest;
import service.messages.QuotationRequest;
import service.messages.QuotationResponse;




public class Broker extends AbstractActor{
    private Set<ActorRef> actorRefs = new HashSet<ActorRef>();
    private int SEED_ID=0;
    public Receive createReceive(){
        return receiveBuilder()
            .match(String.class, 
                msg -> { 
                    
                    if (!msg.equals("register")) return; 
                        actorRefs.add(getSender());  
                        System.out.println(getSender());
            })
            // .match(ApplicationRequest.class,
            //     msg ->{
            //         System.out.println("here");
            //         for (ActorRef ref : actorRefs) {
            //             ref.tell(
            //             new QuotationRequest(SEED_ID, msg.getClientInfo()), getSelf());
            //            }
            //     })
                .match(QuotationResponse.class,
                msg -> {
                        System.out.println(getSender());
                })
                .build(); 
    
            
    }
  
}

