package service.broker;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        if (args.length == 1 ) {
            LocalBrokerService.services = args[0].split(",");
        }
        SpringApplication.run(Application.class, args);
    }
} 

