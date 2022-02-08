package service.core;

import java.util.ArrayList;

public class ClientApplication {
    private ClientInfo clientInfo;
    private int applicationNo;
    private ArrayList<Quotation> quotationList;

    public ClientApplication(ClientInfo clientInfo, int applicationNo, ArrayList<Quotation> quotationList) {
        this.clientInfo = clientInfo;
        this.setApplicationNo(applicationNo);
        this.quotationList = quotationList;
    }

    public ClientApplication(){}

    public int getApplicationNo() {
        return applicationNo;
    }

    public void setApplicationNo(int applicationNo) {
        this.applicationNo = applicationNo;
    }

    
    public ClientInfo getClientInfo() {
        return clientInfo;
    }

    public ArrayList<Quotation> getQuotationList() {
        return quotationList;
    }

    public void setQuotationList(ArrayList<Quotation> quotationList) {
        this.quotationList = quotationList;
    }

    public void setClientInfo(ClientInfo clientInfo) {
        this.clientInfo = clientInfo;
    }
}
