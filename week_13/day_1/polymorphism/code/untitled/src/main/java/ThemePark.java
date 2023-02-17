import attractions.*;
import interfaces.IReviewed;
import stalls.CandyFlossStall;
import stalls.IceCreamStall;
import stalls.Stall;
import stalls.TobaccoStall;
import visitors.Visitor;

import javax.xml.bind.attachment.AttachmentMarshaller;
import java.util.ArrayList;
import java.util.HashMap;

public class ThemePark {
    public ArrayList<Attraction> attractions;

    public ArrayList<Stall> stalls;
    public ArrayList<IReviewed> IReviewsList;
    public HashMap<String, Integer> reviews;

    public ThemePark(ArrayList<Attraction> attractions, ArrayList<Stall> stalls){
        this.attractions = attractions;
        this.stalls = stalls;
        this.reviews = new HashMap<>();

    }

    public ArrayList<IReviewed> getAllReviewed(){
        ArrayList<IReviewed> reviewed = new ArrayList<>();
        reviewed.addAll(attractions);
        reviewed.addAll(stalls);
        return reviewed;
    }

    public void visit(Visitor visitor, Attraction attraction){
        visitor.visitedAttractions.add(attraction);
        attraction.visitCount += 1;
    }

    public HashMap<String, Integer> getReviews(){
        HashMap<String, Integer> reviewMap = new HashMap<>();

        for (IReviewed reviewed : getAllReviewed()) {
            reviewMap.put(reviewed.getName(), reviewed.getRating());
        }
        return reviewMap;




//        for (int i = 0;i < getAllReviewed().size(); i++){
//            this.reviews.put(getAllReviewed().get(i).getName(), getAllReviewed().get(i).getRating());
//            System.out.println(getAllReviewed().get(i));
//        };
//        return this.reviews;
    }
}
