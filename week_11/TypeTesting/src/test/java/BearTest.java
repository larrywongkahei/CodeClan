import org.junit.Before;
import org.junit.Test;
import org.junit.Assert;

public class BearTest {
    private Bear bear;

    @Before
    public void setup (){
        bear = new Bear("Baloo", 12, 95.62, 'f');
    }

    @Test
    public void bearHasName(){
        Assert.assertEquals("Baloo", bear.getName());
    }

    @Test
    public void bearHasAge(){
        Assert.assertEquals(12, bear.getAge());
    }

    @Test
    public void bearHasWeight(){
        Assert.assertEquals(95.62, bear.getWeight(), 0.0);
    }

    @Test
    public void bearIsReadyToHibernate(){
        Assert.assertTrue(bear.readyToHibernate());
    }

    @Test
    public void bearIsNotReadyToHibernate(){
        Bear newBear = new Bear("larry", 20, 70, 'm');
        Assert.assertFalse(newBear.readyToHibernate());
    }

    @Test
    public void bearHasASex(){
        Assert.assertEquals('f', bear.getSex());
    }
}
