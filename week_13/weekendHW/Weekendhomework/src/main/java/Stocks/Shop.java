package Stocks;

import java.util.ArrayList;

public class Shop implements ISell{
    public ArrayList<ISell> items;

    public Shop(ArrayList<ISell> items){
        this.items = items;
    }

    public int getItemsSize() {
        return this.items.size();
    }

    public void addToStock(ISell item){
        this.items.add(item);
    }
    public void removeFromStock(ISell item){
        this.items.removeIf(n -> n == item);
    }


    @Override
    public int calculateMarkup() {
        return this.items.stream()
                .map(each -> each.calculateMarkup())
                .reduce(0,(a,b) -> a+b);
    }
}
