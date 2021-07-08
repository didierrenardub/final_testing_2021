package ar.edu.ub.testing.logging;

import java.util.HashMap;

/** Interface to implement different mutators for the logging strategies.
 *  
 *     Note: while it may seem pointless to let strategies have mutators rather than the `Logger`
 *     itself, truth is that it makes sense because you might want to show different things according
 *     to the strategy. I.e.: while logging into the console you most likely want to keep messages
 *     short, but since the file is searchable you can be open to having more information in there (of
 *     course, when using both strategies at the same time).
 */
public interface Mutator
{
    /**Allows manipulating the received message.
     * 
     * This method, on oncrete classes, will be called by the `Strategy` prior to logging the
     * message.
     * 
     * Args:
     *     message: The message to be logged.
     *     extra_data: [Optional] Dictionary containing information needed by the mutator
     *         to work as expected.
     * 
     * Returns:
     *     String: The mutated version of the original message.
     */
    String mutate(String text, HashMap<String, String> extraData);
}
