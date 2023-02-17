import java.util.ArrayList;

public class Flight {

    private Pilot pilot1;
    private Pilot pilot2;
    private ArrayList<CabinCrewMember> crewList;
    private ArrayList<Passenger> bookedPassenger;
    private Plane plane;
    private String flightNumber;
    private String destination;
    private String departureAirport;
    private String departureTime;

    public Flight(Pilot pilot1, Pilot pilot2, ArrayList<CabinCrewMember> crewList, ArrayList<Passenger> bookedPassenger, Plane plane, String flightNumber, String destination, String departureAirport, String departureTime) {
        this.pilot1 = pilot1;
        this.pilot2 = pilot2;
        this.crewList = crewList;
        this.bookedPassenger = bookedPassenger;
        this.plane = plane;
        this.flightNumber = flightNumber;
        this.destination = destination;
        this.departureAirport = departureAirport;
        this.departureTime = departureTime;
    }

    public Pilot getPilot1() {
        return pilot1;
    }

    public Pilot getPilot2() {
        return pilot2;
    }

    public ArrayList<CabinCrewMember> getCrewList() {
        return crewList;
    }

    public ArrayList<Passenger> getBookedPassenger() {
        return bookedPassenger;
    }

    public Plane getPlane() {
        return plane;
    }

    public String getFlightNumber() {
        return flightNumber;
    }

    public String getDestination() {
        return destination;
    }

    public String getDepartureAirport() {
        return departureAirport;
    }

    public String getDepartureTime() {
        return departureTime;
    }

    public int getSeats(){
        return this.plane.getCapacity();
    }

    public int getSeatsBooked(){
        return this.bookedPassenger.size();
    }

    public boolean checkBookFlight(){
        return this.getSeatsBooked() < this.getSeats();
    }

    public void bookSeat(Passenger passenger){
        if (checkBookFlight()){
            this.bookedPassenger.add(passenger);
        }
    }

    public int getCapacity(){
        return this.plane.getCapacity();
    }

    public double getTotalWeight(){
        return this.plane.getTotalWeight();
    }
}
