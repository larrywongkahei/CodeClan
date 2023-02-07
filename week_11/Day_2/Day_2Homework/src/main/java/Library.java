import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Library {

    private ArrayList<Books> totalBooks;
    private int fullAmount;
    private HashMap<String, Integer> booksByGenre;

    public Library(){
        this.totalBooks = new ArrayList<>();
        this.fullAmount = 3;
        this.booksByGenre = new HashMap<>();
    }

    public int getTotalBooks(){
        return this.totalBooks.size();
    }

    public Map<String, Integer> getBooksRecord(){
        return this.booksByGenre;
    }


    public void addBook(Books book){
        if(this.totalBooks.size() < this.fullAmount){
            this.totalBooks.add(book);
            if(booksByGenre.containsKey(book.getGenre())){
                booksByGenre.put(book.getGenre(), booksByGenre.get(book.getGenre() + 1));
            }else{
                this.booksByGenre.put(book.getGenre(), 1);
            }

        }
    }

    public void removeBook(Books book){
        this.totalBooks.remove(book);
    }
}
