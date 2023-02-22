package com.example.codeclan.pirateservice;

import com.example.codeclan.pirateservice.models.Pirate;
import com.example.codeclan.pirateservice.models.Raid;
import com.example.codeclan.pirateservice.models.Ship;
import com.example.codeclan.pirateservice.repository.PirateRepository;
import com.example.codeclan.pirateservice.repository.RaidRepository;
import com.example.codeclan.pirateservice.repository.ShipRepository;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

@RunWith(SpringRunner.class)
@ActiveProfiles("test") //Indicates it's a test profile so will not run DataLoader
@SpringBootTest
public class PirateserviceApplicationTests {

	@Autowired
	PirateRepository pirateRepository;

	@Autowired
	ShipRepository shipRepository;

	@Autowired
	RaidRepository raidRepository;

	@Test
	public void contextLoads() {
	}

	@Test
	public void createPirateAndShipThenSave(){

		Ship dutchman = new Ship("The Flying Dutchman");
		shipRepository.save(dutchman);
		Pirate jack = new Pirate("jack", "sparrow", 32, dutchman);
		pirateRepository.save(jack);
	}

	@Test
	public void createPirateAndRaidThenSave(){
		Ship pineapple = new Ship("The Flying Pineapple");
		shipRepository.save(pineapple);
		Pirate spongeBob = new Pirate("SpongeBob", "SquarePants", 8, pineapple);
		pirateRepository.save(spongeBob);

		Raid raid = new Raid("Tortuga", 100);
		raidRepository.save(raid);

		spongeBob.addRaid(raid);
		raid.addPirate(spongeBob);
		raidRepository.save(raid);
		
	}

	@Test
	public void canFindPiratesOver30(){
		List<Pirate> foundPirates = pirateRepository.findByAgeGreaterThan(30);
		assertTrue(foundPirates.size() > 0);
	}

	@Test
	public void canFindPirateByName(){
		List<Pirate> foundPirates = pirateRepository.findByFirstName("Horatio");
		assertEquals(1, foundPirates.size());
	}

	@Test
	public void canFindRaidByLocation(){
		List<Raid> foundRaids = raidRepository.findByLocation("Tortuga");
		assertEquals(1, foundRaids.size());
	}

	@Test
	public void canFindShipByPirateFirstName(){
		List<Ship> foundShips = shipRepository.findByPiratesFirstName("Henry");
		assertEquals(1, foundShips.size());

	}

	@Test
	public void canFindRaidsByShip(){
		List<Raid> foundRaids = raidRepository.findByPiratesShip(shipRepository.getById(7L));
		assertEquals(1, foundRaids.size());
	}

}
