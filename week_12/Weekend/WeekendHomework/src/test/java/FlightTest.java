import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

public class FlightTest {

    Flight flight;
    Pilot pilot1;
    Pilot pilot2;
    CabinCrewMember cabinCrewMember1;
    CabinCrewMember cabinCrewMember2;
    CabinCrewMember cabinCrewMember3;
    ArrayList<CabinCrewMember> crewMembersList;
    Passenger passenger1;
    Passenger passenger2;
    Passenger passenger3;
    Passenger passenger4;
    ArrayList<Passenger> passengerList;
    Plane plane;

    @Before
    public void setup(){
//        Set up Pilot
        pilot1 = new Pilot("LarryAgain", "Pilot", "3325498");
        pilot2 = new Pilot("CindyAgain", "Pilot", "3322312");
//        Set up CrewMemberList
        cabinCrewMember1 = new CabinCrewMember("Mary", "Purser");
        cabinCrewMember2 = new CabinCrewMember("Peter", "Captain");
        cabinCrewMember3 = new CabinCrewMember("Billy", "First Officer");
        crewMembersList = new ArrayList<CabinCrewMember>();
        crewMembersList.add(cabinCrewMember1);
        crewMembersList.add(cabinCrewMember2);
        crewMembersList.add(cabinCrewMember3);
//        Set up Passengers
        passenger1 = new Passenger("Larry", 3);
        passenger2 = new Passenger("Brian", 1);
        passenger3 = new Passenger("Joe", 4);
        passenger4 = new Passenger("Joey", 5);
        passengerList = new ArrayList<Passenger>();
        passengerList.add(passenger1);
        passengerList.add(passenger2);
        passengerList.add(passenger3);
//        Set up Plane
        plane = new Plane(PlaneType.BOEING747);
//        Set up flight
        flight = new Flight(pilot1, pilot2, crewMembersList, passengerList, plane, "TL723", "EDI", "GLA", "13:25");

    }

    @Test
    public void checkFlightCouldReturnSeats(){
        Assert.assertEquals(3, flight.getSeats());
    }

    @Test
    public void checkFlightCouldReturnSeatBooked(){
        Assert.assertEquals(3, flight.getSeatsBooked());
    }

    @Test
    public void checkCouldBookFlightFailed(){
        Assert.assertFalse(flight.checkBookFlight());
    }

    @Test
    public void checkCouldBookFlight(){
        passengerList.remove(0);
        Assert.assertTrue(flight.checkBookFlight());
    }

    @Test
    public void checkBookFlightFailed(){
        Assert.assertEquals(3, flight.getSeatsBooked());
        flight.bookSeat(passenger4);
        Assert.assertEquals(3, flight.getSeatsBooked());
    }

    @Test
    public void checkBookFlight(){
        Assert.assertEquals(3, flight.getSeatsBooked());
        passengerList.remove(0);
        Assert.assertEquals(2, flight.getSeatsBooked());
        flight.bookSeat(passenger4);
        Assert.assertEquals(3, flight.getSeatsBooked());
    }

    @Test
    public void checkFlightGetCapacity(){
        Assert.assertEquals(3, flight.getCapacity());
    }

    @Test
    public void checkFlightGetTotalWeight(){
        Assert.assertEquals(2000, flight.getTotalWeight(), 0.0);
    }

    @Test
    public void flightCouldgetBaggageWeightForPassenger() {
        Assert.assertEquals(400, FlightManager.getBaggageWeightForPassenger(flight), 0.00);
    }

    @Test
    public void flightCouldgetBaggageForPasserngers() {
        Assert.assertEquals(1200, FlightManager.getBaggageForPasserngers(flight), 0.00);
    }

    @Test
    public void flightCouldgetBaggageRemains() {
        Assert.assertEquals(1200, FlightManager.getBaggageRemains(flight), 0.00);
    }
}
