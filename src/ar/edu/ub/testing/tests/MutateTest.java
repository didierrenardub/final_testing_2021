package ar.edu.ub.testing;


import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


import java.util.ArrayList;
import java.util.HashMap;
public class MutateTest {

    @Test
    public void Mutate_ValidText_And_DataTest(){
        String text = ("Buen Dia");
        String MutatedText = Strategy.mutate(text,Data);
        assertEquals("Buen Dia",MutatedText);
    }

    @Test
    public void Mutate_EmptyText_And_NullData_Test(){
        String MutatedText = Strategy.mutate(text,null);
        assertEquals("",MutatedText);
    }

    @Test
    public void AddMutatorTest(){
        mutators.add(Strategy.addMutator(mutator.mutate("a",Data)));
        assertTrue(mutators.contains(mutator));
    }

    @Test
    public void RemoveFilterTest(){
        mutators.add(Strategy.addFilter(mutator.mutate(text,Data)));
        Strategy.removeFilter(mutator.mutate(text,Data));
        assertEquals("",mutators);
    }

    @Test
    public void Clear_Mutator_Test(){
        mutators.add(Strategy.addMutator(mutator));
        Strategy.clearMutators();
        assertEquals("",mutators);

    }
    String text = new String("");
    HashMap<String,String> Data;
    Mutator mutator;
    private ArrayList<Mutator>  mutators= new ArrayList<Mutator>();
}
