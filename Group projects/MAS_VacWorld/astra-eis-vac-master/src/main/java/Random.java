import java.math.*;

import astra.core.Module.TERM;

public class Random extends astra.core.Module {
    @TERM
    public double randomIntDir() {
        double random = Math.random() * 75;
        return random;
    }

    @TERM
    public int randomIntDistance() {
        int random = (int)Math.floor((Math.random() * 2) + 1);
        return random;
    }

    @TERM
    public double randomInt() {
        double random = Math.random() * 100;
        return random;
    }
}