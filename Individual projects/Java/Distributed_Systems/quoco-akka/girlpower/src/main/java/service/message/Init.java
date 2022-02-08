package service.message;

import service.core.QuotationService;
import akka.actor.ActorRef;

public class Init {
    private QuotationService service;
    
    public Init(QuotationService service) {
        this.service = service;
        
    }

    public QuotationService getQuotationService() {
        return service;
    }

}
