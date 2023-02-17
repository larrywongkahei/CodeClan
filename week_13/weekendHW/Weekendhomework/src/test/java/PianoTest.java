import Stocks.Pianos;
import Stocks.Type;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class PianoTest {

    public Pianos piano;
    @Before
    public void setup(){
        piano = new Pianos("wood", "gray", Type.KEYBOARD, 88, 4500);
    }

    @Test
    public void pianoHasKey(){
        Assert.assertEquals(88, piano.getKeys());
    }

    @Test
    public void pianoCanPlay(){
        Assert.assertEquals("I ~ am ~ Pi ~ Pi ~ Pi ~ an ~ no", piano.play());
    }

    @Test
    public void pianoHasPrice(){
        Assert.assertEquals(4500, piano.getPrice());
    }

}
