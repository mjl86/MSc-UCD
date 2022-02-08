package service.messages;




import service.core.ClientInfo;


public class ApplicationRequest implements MySerializable{
   
    private ClientInfo clientinfo;
    public ApplicationRequest(ClientInfo clientinfo) {
        this.clientinfo=clientinfo;
    }
    public ApplicationRequest() {}

    public ClientInfo getClientInfo(){
        return clientinfo;
    }
}
