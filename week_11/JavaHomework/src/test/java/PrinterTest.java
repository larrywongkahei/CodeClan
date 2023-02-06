import org.junit.Before;
import org.junit.Test;
import org.junit.Assert;

public class PrinterTest {

    private Printer printer;

    @Before
    public void setup(){
        printer = new Printer(100, 1000);
    }

    @Test
    public void getTheNumberOfPaper(){
        Assert.assertEquals(100, printer.getPaper());
    }

    @Test
    public void checkIfAbleToPrint(){
        printer.print(10, 2);
        Assert.assertEquals(80, printer.getPaper());
        Assert.assertEquals(980, printer.getToner());
    }

    @Test
    public void checkIfAbleToPrint2(){
        printer.print(5, 3);
        Assert.assertEquals(85, printer.getPaper());
        Assert.assertEquals(985, printer.getToner());
    }

    @Test
    public void checkIfAbleToStopPrinting(){
        printer.print(10, 10);
        Assert.assertEquals(0, printer.getPaper());
        Assert.assertEquals(900, printer.getToner());

        Assert.assertFalse(printer.print(1, 2));
        Assert.assertEquals(900, printer.getToner());
    }

    @Test
    public void checkIfAbleToStopPrinting2(){
        Assert.assertTrue(printer.print(10, 10));
        Assert.assertEquals(900, printer.getToner());

        Assert.assertFalse(printer.print(1, 2));
        Assert.assertEquals(900, printer.getToner());
    }
}
