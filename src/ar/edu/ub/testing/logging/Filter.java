package ar.edu.ub.testing.logging;

import java.util.HashMap;

/** Used to block messages from being logged based on the `Filter`'s criteria.
 *
 * Every `LogStrategy` may have different filters. Note this is just the interface.
 */
public interface Filter
{
    /** Determine if a message should be logged or not.
     *
     * Args:
     *    text: The message to check if it should be filtered out or not.
     *    extraData: Other parameters supplied along with the message aimed for the `Mutator`s
     *        and/or strategies, which could also be taken into account for message filtering. You
     *        could also expect parameters to come here for your filter to act.
     * 
     * Returns:
     *     bool: `true` if the message should not be displayed in the log, `false` otherwise.
     */
     boolean filter(String text, HashMap<String, String> extraData);
}
