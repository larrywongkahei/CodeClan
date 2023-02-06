public class Printer {

    private int paper;
    private int toner;


    public Printer(int paper, int toner){
        this.paper = paper;
        this.toner = toner;
    }

    public int getPaper(){
        return this.paper;
    }

    public int getToner(){
        return this.toner;
    }

    public boolean print(int pages, int copies){
        if(this.paper >= pages * copies){
            this.paper -= pages * copies;
            this.toner -= pages * copies;
            return true;
        }
        return false;
    }
}
