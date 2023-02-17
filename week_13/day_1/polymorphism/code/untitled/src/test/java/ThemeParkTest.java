import attractions.*;
import interfaces.IReviewed;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import stalls.CandyFlossStall;
import stalls.IceCreamStall;
import stalls.Stall;
import stalls.TobaccoStall;
import visitors.Visitor;

import java.util.ArrayList;

public class ThemeParkTest {

    public ThemePark themePark;
    public Dodgems dodgems;
    public Park park;
    public Playground playground;
    public Rollercoaster rollercoaster;

    public ArrayList<IReviewed> IReviewsList;

    public CandyFlossStall candyFlossStall;
    public IceCreamStall iceCreamStall;
    public TobaccoStall tobaccoStall;
    public Visitor visitor;
    public ArrayList<Attraction> attractions;
    public ArrayList<Stall> stalls;



    @Before
    public void setup() {
        visitor = new Visitor(20, 170, 2000);
        dodgems = new Dodgems("Larry", 5);
        park = new Park("Cindy", 5);
        playground = new Playground("Fun", 5);
        rollercoaster = new Rollercoaster("roller", 5);
        IReviewsList = new ArrayList<>();
        candyFlossStall = new CandyFlossStall("CandyStall", "Larry", 5, "Center");
        iceCreamStall = new IceCreamStall("IceCreamStall", "Larry", 5, "Left");
        tobaccoStall = new TobaccoStall("TobaccoStall", "Larry", 5, "Right");
        attractions = new ArrayList<>();
        stalls = new ArrayList<>();
        attractions.add(dodgems);
        attractions.add(park);
        attractions.add(playground);
        attractions.add(rollercoaster);
        stalls.add(candyFlossStall);
        stalls.add(iceCreamStall);
        stalls.add(tobaccoStall);
        themePark = new ThemePark(attractions, stalls);

    }
    @Test
    public void checkThemeParkCouldVisit(){
        Assert.assertEquals(0, visitor.visitedAttractions.size());
        Assert.assertEquals(0, rollercoaster.visitCount);
        themePark.visit(visitor, rollercoaster);
        Assert.assertEquals(1, visitor.visitedAttractions.size());
        Assert.assertEquals(1, rollercoaster.visitCount);

    }

    @Test
    public void checkCouldReturnReviews(){
//        System.out.println(themePark.getAllReviewed());
        System.out.println(themePark.getReviews());
        Assert.assertEquals(0, 0);

    }
}


