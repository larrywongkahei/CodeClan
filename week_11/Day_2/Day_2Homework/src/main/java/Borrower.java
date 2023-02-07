import java.util.ArrayList;

public class Borrower {

    private ArrayList<Books> collection;

    public Borrower(){
        this.collection = new ArrayList<>();
    }

    public int getCollection(){
        return this.collection.size();
    }

    public void borrow(Books book, Library library){
        this.collection.add(book);
        library.removeBook(book);
    }
}
