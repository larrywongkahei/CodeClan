import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import staff.management.Manager;

public class ManagerTest {

    private Manager manager;


    @Before
    public void setup(){
        manager = new Manager("Larry", "AB12345C", 30000, "Finance");
    }

    @Test
    public void managerHasName(){
        Assert.assertEquals("Larry", manager.getName());
    }

    @Test
    public void managerHasNINumber(){
        Assert.assertEquals("AB12345C", manager.getNiNumber());
    }

    @Test
    public void managerHasSalary(){
        Assert.assertEquals(30000, manager.getSalary(), 0.0);
    }

    @Test
    public void managerHasDeptName(){
        Assert.assertEquals("Finance", manager.getDeptName());
    }

    @Test
    public void managerCouldBeRaiseSalary(){
        manager.raiseSalary(30);
        Assert.assertEquals(30030, manager.getSalary(), 0.0);
    }

    @Test
    public void managerCouldNotBeRaiseNegativeSalary(){
        manager.raiseSalary(-10);
        Assert.assertEquals(30000, manager.getSalary(), 0.0);
    }

    @Test
    public void managerCouldBePaidBonus(){
        Assert.assertEquals(300, manager.payBonus(), 0.0);
    }

    @Test
    public void managerCouldChangeName(){
        manager.changeName("Ryan");
        Assert.assertEquals("Ryan", manager.getName());
    }

}
