import com.sun.xml.internal.ws.policy.AssertionSet;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.awt.print.Book;

public class BooksTest {

    private Books book1;
    private Books book2;
    private Books book3;


    @Before
    public void setup(){
        book1 = new Books("First Book", "Larry", "Fiction");
        book2 = new Books("Second Book", "Larry2", "non-Fiction");
        book3 = new Books("Third Book", "Larry3", "Fantasy");

    }

    @Test
    public void bookHastitle(){
        Assert.assertEquals("First Book", book1.getTitle());
        Assert.assertEquals("Second Book", book2.getTitle());
        Assert.assertEquals("Third Book", book3.getTitle());
    }

    @Test
    public void bookHasAuthor(){
        Assert.assertEquals("Larry", book1.getAuthor());
        Assert.assertEquals("Larry2", book2.getAuthor());
        Assert.assertEquals("Larry3", book3.getAuthor());
    }

    @Test
    public void bookHasGenre(){
        Assert.assertEquals("Fiction", book1.getGenre());
        Assert.assertEquals("non-Fiction", book2.getGenre());
        Assert.assertEquals("Fantasy", book3.getGenre());
    }


}
