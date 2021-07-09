package ar.edu.ub.testing;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


import java.util.ArrayList;
import java.util.HashMap;

class logTest {


    @Test
    public void log_Test(){
        filters.add(Strategy.addFilter(filter.filter(text,Data)));
        mutators.add(Strategy.addMutator(mutator.mutate("ABC",null)));
        boolean log = Strategy.log(text,Data);
        assertTrue(log);
    }




    String text = new String("");
    HashMap<String, String> Data;
    Mutator mutator;
    Filter filter;
    private ArrayList<Filter> filters = new ArrayList<Filter>();
    private ArrayList<Mutator>  mutators= new ArrayList<Mutator>();

}