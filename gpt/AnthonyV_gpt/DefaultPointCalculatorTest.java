// ORIGINAL CODE
/*
package nl.tudelft.jpacman.points;
//import nl.tudelft.jpacman.level.Pellet;
import nl.tudelft.jpacman.level.Player;
import nl.tudelft.jpacman.level.PlayerFactory;
//import nl.tudelft.jpacman.sprite.EmptySprite;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import nl.tudelft.jpacman.sprite.PacManSprites;

public class DefaultPointCalculatorTest {

    private DefaultPointCalculator DPC = new DefaultPointCalculator();

    private static final PacManSprites SPRITE_STORE = new PacManSprites();
    private PlayerFactory Factory = new PlayerFactory(SPRITE_STORE);
    private Player ThePlayer = Factory.createPacMan();
    //private EmptySprite TheSprite = new EmptySprite();
    @Test
    void testConsumedAPellet(){
        //DPC.consumedAPellet(ThePlayer,new Pellet(1,TheSprite));
        assertThat(ThePlayer.getScore()).isEqualTo(1);
    }
}
*/

// CHAT GPT CODE (old, DID NOT WORK FOR TESTING) (Task 2.1)
/*
package nl.tudelft.jpacman.points;

import nl.tudelft.jpacman.level.Player;
import nl.tudelft.jpacman.level.PlayerFactory;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import nl.tudelft.jpacman.sprite.PacManSprites;

public class DefaultPointCalculatorTest {

    private DefaultPointCalculator defaultPointCalculator;
    private PlayerFactory playerFactory;
    private Player player;

    @BeforeEach
    void setUp() {
        PacManSprites spriteStore = new PacManSprites();
        defaultPointCalculator = new DefaultPointCalculator();
        playerFactory = new PlayerFactory(spriteStore);
        player = playerFactory.createPacMan();
    }

    @Test
    void testConsumedAPellet() {
        // Pellet pellet = new Pellet(1, new EmptySprite());
        defaultPointCalculator.consumedAPellet(player, pellet);
        assertThat(player.getScore()).isEqualTo(1);
    }
}
*/
// NEW CHATGPT CORRECTED CODE (FOR TESTING) (Task 2.1)
/*
package nl.tudelft.jpacman.points;

import nl.tudelft.jpacman.level.Pellet;
import nl.tudelft.jpacman.level.Player;
import nl.tudelft.jpacman.level.PlayerFactory;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import nl.tudelft.jpacman.sprite.PacManSprites;
import nl.tudelft.jpacman.sprite.EmptySprite;

// needs better documentation
public class DefaultPointCalculatorTest {

    private DefaultPointCalculator defaultPointCalculator;
    private PlayerFactory playerFactory;
    private Player player;

    @BeforeEach
    void setUp() {
        PacManSprites spriteStore = new PacManSprites();
        defaultPointCalculator = new DefaultPointCalculator();
        playerFactory = new PlayerFactory(spriteStore);
        player = playerFactory.createPacMan();
    }

    @Test
    void testConsumedAPellet() {
        Pellet pellet = new Pellet(1, new EmptySprite());
        defaultPointCalculator.consumedAPellet(player, pellet);
        assertThat(player.getScore()).isEqualTo(1);
    }
}
*/
// NEW CHATGPT CORRECTED AND DOCUMENTED CODE (Task 2.2)
package nl.tudelft.jpacman.points;

import nl.tudelft.jpacman.level.Pellet;
import nl.tudelft.jpacman.level.Player;
import nl.tudelft.jpacman.level.PlayerFactory;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import nl.tudelft.jpacman.sprite.PacManSprites;
import nl.tudelft.jpacman.sprite.EmptySprite;

/**
 * Unit tests for DefaultPointCalculator class.
 */
public class DefaultPointCalculatorTest {

    private DefaultPointCalculator defaultPointCalculator;
    private PlayerFactory playerFactory;
    private Player player;

    /**
     * Setting up the necessary objects for testing.
     */
    @BeforeEach
    void setUp() {
        // Creating PacManSprites object for sprite storage
        PacManSprites spriteStore = new PacManSprites();
        // Instantiating DefaultPointCalculator
        defaultPointCalculator = new DefaultPointCalculator();
        // Instantiating PlayerFactory
        playerFactory = new PlayerFactory(spriteStore);
        // Creating a PacMan player
        player = playerFactory.createPacMan();
    }

    /**
     * Test case to verify the consumedAPellet method of DefaultPointCalculator.
     * It checks if the player's score increases by 1 after consuming a pellet.
     */
    @Test
    void testConsumedAPellet() {
        // Creating a pellet with a score value of 1
        Pellet pellet = new Pellet(1, new EmptySprite());
        // Invoking consumedAPellet method to simulate pellet consumption by the player
        defaultPointCalculator.consumedAPellet(player, pellet);
        // Asserting that the player's score is incremented by 1
        assertThat(player.getScore()).isEqualTo(1);
    }
}

