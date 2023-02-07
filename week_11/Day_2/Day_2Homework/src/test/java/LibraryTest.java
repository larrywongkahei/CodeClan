import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class LibraryTest {

    private Library library;
    private Books book1;
    private Books book2;
    private Books book3;
    private Books book4;

    @Before
    public void setup(){
        library = new Library();
        book1 = new Books("First Book", "Larry", "Fiction");
        book2 = new Books("First Book", "Larry", "non-Fiction");
        book3 = new Books("First Book", "Larry", "Fiction");
        book4 = new Books("First Book", "Larry", "Fiction");
        library.addBook(book1);
    }

    @Test
    public void haveTotalBooks(){
        Assert.assertEquals(1, library.getTotalBooks());
    }

    @Test
    public void canAddBooks(){
        Assert.assertEquals(1, library.getTotalBooks());
        Assert.assertTrue(library.getBooksRecord().containsKey(book1.getGenre()));
        Assert.assertFalse(library.getBooksRecord().containsKey(book2.getGenre()));

        library.addBook(book2);
        Assert.assertTrue(library.getBooksRecord().containsKey(book2.getGenre()));

    }

    @Test
    public void canNotAddBooksIfFull(){
        library.addBook(book2);
        library.addBook(book3);
        Assert.assertEquals(3, library.getTotalBooks());
        library.addBook(book4);
        Assert.assertEquals(3, library.getTotalBooks());

    }

    @Test
    public void canRemoveBook(){
        library.addBook(book2);
        library.addBook(book3);
        Assert.assertEquals(3, library.getTotalBooks());
        library.removeBook(book1);
        Assert.assertEquals(2, library.getTotalBooks());



    }
}
