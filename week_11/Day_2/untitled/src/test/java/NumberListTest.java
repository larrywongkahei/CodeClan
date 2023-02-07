import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

public class NumberListTest {

    private NumberList myNumbers;

    @Before
    public void setup(){

        ArrayList<Integer> testNumbers = new ArrayList<>();
        testNumbers.add(1);
        testNumbers.add(2);
        testNumbers.add(3);
        testNumbers.add(4);
        myNumbers = new NumberList(testNumbers);
    }

    @Test
    public void hasNumberOfEntries(){
        Assert.assertEquals(4, myNumbers.getNumberCount());
    }

    @Test
    public void canAddNumberToList(){
        myNumbers.addNumber(12);
        Assert.assertEquals(12, myNumbers.getNumerAtIndex(4));
    }

    @Test
    public void canGetFirstNumber(){
        Assert.assertEquals(1, myNumbers.getNumerAtIndex(0));
    }

    @Test
    public void canGetTotal(){
        Assert.assertEquals(10, myNumbers.getTotal());
    }
}
