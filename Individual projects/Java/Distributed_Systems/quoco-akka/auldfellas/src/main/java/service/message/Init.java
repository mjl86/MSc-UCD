package service.message;

import service.core.QuotationService;


public class Init {
    private QuotationService service;
    
    public Init(QuotationService service) {
        this.service = service;
        
    }
    public Init(){}

    public QuotationService getQuotationService() {
        return service;
    }

}
