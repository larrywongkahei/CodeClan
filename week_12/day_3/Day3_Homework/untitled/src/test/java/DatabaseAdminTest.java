import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import staff.techStaff.DatabaseAdmin;

public class DatabaseAdminTest {
        private DatabaseAdmin admin;

        @Before
        public void setup(){
            admin = new DatabaseAdmin("John", "AB23423D", 27000);
        }

        @Test
        public void adminHasName(){
            Assert.assertEquals("John", admin.getName());
        }

        @Test
        public void adminHasNINumber(){
            Assert.assertEquals("AB23423D", admin.getNiNumber());
        }

        @Test
        public void adminHasSalary(){
            Assert.assertEquals(27000, admin.getSalary(), 0.0);
        }

        @Test
        public void adminCouldBeRaiseSalary(){
            admin.raiseSalary(500);
            Assert.assertEquals(27500, admin.getSalary(), 0.0);
        }

        @Test
        public void adminCouldNotBeRaiseNegativeSalary(){
            admin.raiseSalary(-10);
            Assert.assertEquals(27000, admin.getSalary(), 0.0);
        }

        @Test
        public void adminCouldChangeName(){
            admin.changeName("Billy");
            Assert.assertEquals("Billy", admin.getName());
            }

        @Test
        public void adminCouldBePaidBonus(){
            Assert.assertEquals(270, admin.payBonus(), 0.0);
        }
}
