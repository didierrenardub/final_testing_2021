package ar.edu.ub.testing;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class FilterTest {

    @Test
    public void AddFilterTest(){
        filters.add(Strategy.addFilter(filter.filter(text,Data)));
        assertTrue(filters.contains(filter));
    }

    @Test
    public void RemoveFilterTest(){
        filters.add(Strategy.addFilter(filter.filter(text,Data)));
        Strategy.removeFilter(filter.filter(text,Data));
        assertEquals("",filters);
    }


    String text = new String("");
    HashMap<String,String> Data;
    Filter filter;
    private ArrayList<Filter> filters = new ArrayList<Filter>();

}
