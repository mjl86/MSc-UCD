package service.message;

import java.io.Serializable;

import service.core.ClientInfo;
import service.core.Quotation;

public class QuotationResponseMessage implements Serializable { 
    public long id; 
    public Quotation quotation;
    public ClientInfo info; 
    public QuotationResponseMessage(long id, Quotation quotation) { 
    this.id = id; 
    this.quotation = quotation; 
    } 
} 
