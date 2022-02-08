package service.messages;

import java.util.ArrayList;


import service.core.ClientInfo;
import service.core.Quotation;

public class ApplicationResponse implements MySerializable{
    private ClientInfo clientinfo;
    private ArrayList<Quotation> quotations;
    public ApplicationResponse(ClientInfo clientinfo, ArrayList<Quotation> quotations){
        this.clientinfo=clientinfo;
        this.quotations=quotations;
    }
    
    public ApplicationResponse(){}

    public ClientInfo getClientInfo(){
        return clientinfo;
    }

    public ArrayList<ClientInfo> getQuotations(){
        return quotations;
    }

}
