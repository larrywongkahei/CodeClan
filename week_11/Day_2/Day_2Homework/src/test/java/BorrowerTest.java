import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class BorrowerTest {

    private Borrower borrower;
    private Books book1;
    private Books book2;
    private Library library;

    @Before
    public void setup(){
        borrower = new Borrower();
        library = new Library();
        book1 = new Books("First Book", "Larry", "Fiction");
        book2 = new Books("First Book", "Larry", "Fiction");
        library.addBook(book1);
        library.addBook(book2);
    }

    @Test
    public void borrowerHasCollection(){
        Assert.assertEquals(0, borrower.getCollection());
    }

    @Test
    public void borrowBooksFromLibrary(){
        Assert.assertEquals(0, borrower.getCollection());
        borrower.borrow(book1, library);
        Assert.assertEquals(1, library.getTotalBooks());
        Assert.assertEquals(1, borrower.getCollection());

    }
}
