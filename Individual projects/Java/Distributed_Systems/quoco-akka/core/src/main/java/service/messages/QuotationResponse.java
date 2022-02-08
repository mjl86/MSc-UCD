package service.messages;

import service.core.Quotation;

public class QuotationResponse implements MySerializable{ 
    private int id; 
    private Quotation quotation; 

    public QuotationResponse(int id, Quotation quotation) { 
    this.setId(id); 
    this.setQuotation(quotation); 
    } 

    public QuotationResponse(){}
    
    public Quotation getQuotation() {
        return quotation;
    }
    public void setQuotation(Quotation quotation) {
        this.quotation = quotation;
    }
    // add get and set methods for each field 
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
   } 
