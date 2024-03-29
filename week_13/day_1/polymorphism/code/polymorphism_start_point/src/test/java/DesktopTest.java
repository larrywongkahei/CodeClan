import org.junit.Before;
import org.junit.Test;
import org.junit.Assert

import static org.junit.Assert.assertEquals;

public class DesktopTest {
    Desktop desktop;

    @Before
    public void before() {
        desktop = new Desktop("Keith's Desktop", "Apple", "Macbook Pro");
    }

    @Test
    public void hasName(){
        assertEquals("Keith's Desktop", desktop.getName());
    }

    @Test
    public void hasMake(){
        assertEquals("Apple", desktop.getMake());
    }

    @Test
    public void hasModel(){
        assertEquals("Macbook Pro", desktop.getModel());
    }

    @Test
    public void canConnect() {
        Assert.assertEquals("Connecting to network: Codeclan", desktop.connect("Codeclan"));
    }
}
