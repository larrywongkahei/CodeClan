import org.junit.Assert;
import org.junit.Test;

public class CarTest {

    @Test
    public void canConvertCar(){
        Car car = new Car("Tesla", 3);

        String message = Converter.process(car);

        Assert.assertEquals("Car data", message);
    }
}
