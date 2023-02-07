import org.junit.Before;
import org.junit.Test;
import org.junit.Assert;

public class WordCollectionTest {

    private WordCollection myWords;

    @Before
    public void setup(){
        myWords = new WordCollection();
    }
    @Test
    public void canGetWordCount(){
        Assert.assertEquals(0, myWords.getWordCount());
    }

}
