import Stocks.*;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

public class ShopTest {
    public Shop shop;
    public Guitars guitars;
    public Pianos pianos;
    public Ukeleles ukeleles;
    public DrumSticks drumSticks;
    public GuitarStrings guitarStrings;
    public GuitarStrings guitarStrings2;

    @Before
    public void setup(){
        guitars = new Guitars("wood", "brown", Type.STRINGS, 6, 3000);
        pianos = new Pianos("wood", "gray", Type.KEYBOARD, 88, 4500);
        ukeleles = new Ukeleles("wood", "black", Type.STRINGS, 5, 1500);
        drumSticks = new DrumSticks(150);
        guitarStrings = new GuitarStrings(260);
        guitarStrings2 = new GuitarStrings(260);
        ArrayList<ISell> stockItems = new ArrayList<>();
        stockItems.add(guitars);
        stockItems.add(pianos);
        stockItems.add(ukeleles);
        stockItems.add(drumSticks);
        stockItems.add(guitarStrings);
        shop = new Shop(stockItems);
    }

    @Test
    public void shopHasStockItems(){
        Assert.assertEquals(5, shop.getItemsSize());
    }

    @Test
    public void shopCouldRemoveItem(){
        Assert.assertEquals(5, shop.getItemsSize());
        shop.removeFromStock(guitars);
        Assert.assertEquals(4, shop.getItemsSize());
    }

    @Test
    public void shopCouldAddItem(){
        Assert.assertEquals(5, shop.getItemsSize());
        shop.addToStock(guitarStrings2);
        Assert.assertEquals(6, shop.getItemsSize());
    }

    @Test
    public void testCalculateMarkup(){
        Assert.assertEquals(9410, shop.calculateMarkup());
    }
}
