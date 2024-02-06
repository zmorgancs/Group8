
package nl.tudelft.jpacman.level;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import nl.tudelft.jpacman.board.Board;
import nl.tudelft.jpacman.board.Direction;
import nl.tudelft.jpacman.board.Square;
import nl.tudelft.jpacman.board.Unit;
import nl.tudelft.jpacman.npc.Ghost;
import nl.tudelft.jpacman.sprite.PacManSprites;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.MockitoAnnotations;

import java.util.ArrayList;
import java.util.List;

class LevelTest {

    private Board board;
    private List<Ghost> ghosts;
    private List<Square> startSquares;
    private CollisionMap collisionMap;
    private Level level;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.initMocks(this);

        // Set up the mock board
        board = mock(Board.class);
        when(board.getWidth()).thenReturn(5);
        when(board.getHeight()).thenReturn(5);

        // Create a list for ghosts and squares
        ghosts = new ArrayList<>();
        startSquares = new ArrayList<>();

        // Set up the mock squares and the occupants for each square
        Square mockSquare = mock(Square.class);
        // Assume that each square has an empty list of occupants by default
        when(mockSquare.getOccupants()).thenReturn(new ArrayList<>());

        // Stub the behavior of board.squareAt(x, y) to return the mock square
        for (int x = 0; x < board.getWidth(); x++) {
            for (int y = 0; y < board.getHeight(); y++) {
                when(board.squareAt(x, y)).thenReturn(mockSquare);
            }
        }

        // Add one square to the startSquares list for player start positions
        startSquares.add(mockSquare);

        // Set up a mock collision map
        collisionMap = mock(CollisionMap.class);

        // Initialize the level with the mock objects
        level = new Level(board, ghosts, startSquares, collisionMap);
    }

    @Test
    void levelShouldNotBeInProgressInitially() {
        assertFalse(level.isInProgress());
    }

    @Test
    void levelShouldBeInProgressAfterStart() {
        level.start();
        assertTrue(level.isInProgress());
    }

    @Test
    void levelShouldNotBeInProgressAfterStop() {
        level.start();
        level.stop();
        assertFalse(level.isInProgress());
    }
}

