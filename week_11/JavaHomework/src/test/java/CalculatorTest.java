import org.junit.Test;
import org.junit.Assert;

public class CalculatorTest {

    @Test
    public void checkIfAbleAdd(){
        Assert.assertEquals(8, Calculator.add(3, 5));
    }

    @Test
    public void checkIfAbleAdd2(){
        Assert.assertEquals(16, Calculator.add(9, 7));
    }

    @Test public void checkIfAbleToSubtract(){
        Assert.assertEquals(9, Calculator.subtract(16, 7));
    }

    @Test public void checkIfAbleToSubtract2(){
        Assert.assertEquals(3, Calculator.subtract(16, 13));
    }

    @Test public void checkIfAbleToMultiply(){
        Assert.assertEquals(30, Calculator.multiply(3, 10));
    }

    @Test public void checkIfAbleToMultiply2(){
        Assert.assertEquals(45, Calculator.multiply(9, 5));
    }

    @Test public void checkIfAbleToDivide(){
        Assert.assertEquals(5, Calculator.divide(45, 9), 0.0);
    }

    @Test public void checkIfAbleToDivide2(){
        Assert.assertEquals(3, Calculator.divide(45, 15), 0.0);
    }
}
