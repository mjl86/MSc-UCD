package service.messages;

import service.core.ClientInfo;

public class QuotationRequest implements MySerializable{ 
    private int id; 
    private ClientInfo clientInfo; 
    public QuotationRequest(int id, ClientInfo clientInfo) { 
    this.setId(id); 
    this.setClientInfo(clientInfo); 
    } 

    public QuotationRequest(){}
    
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    // add get and set methods for each field 
    public ClientInfo getClientInfo() {
        return clientInfo;
    }
    public void setClientInfo(ClientInfo clientInfo) {
        this.clientInfo = clientInfo;
    }
   } 
