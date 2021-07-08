package ar.edu.ub.testing.logging;

import java.util.ArrayList;
import java.util.HashMap;

/** Nucleates the different logging strategies to use them in a centralized way.
 * 
 * `Logger` is a `Strategy` itself, which allows to pre-mutate all messages with the same `Mutator`
 * prior to forwarding the messages to its inner strategies, which can in turn have their own
 * mutators.
 * 
 * Strategies can still be used individually, though.
 */
public class Logger extends LogStrategy
{
    /** Initialize the `Logger` with the given strategies, if any.
     * 
     * Note that for the `Logger` to work you need to supply at least one strategy, otherwise, the
     * `Logger` itself does nothing with the messages.
     */
    public Logger()
    {
        this(null);
    }

    /** Initialize the `Logger` with the given strategies, if any.
     * 
     * Note that for the `Logger` to work you need to supply at least one strategy, otherwise, the
     * `Logger` itself does nothing with the messages.
     * 
     * Args:
     *     strategies: A list of `LogStrategy` objects that will define the `Logger` behaves.
     */
    public Logger(ArrayList<LogStrategy> strategies)
    {
        super();
        if (strategies != null)
        {
            this.strategies = strategies;
        }
    }

    /** Adds the given `LogStrategy` to the current `Logger`.
     * 
     * Args:
     *     strategy: The `LogStrategy` object that should be applied when logging with the current
     *         `Logger`.
     * 
     * Returns:
     *     boolean: Confirmation whether the strategy has been added or not.
     */
    public boolean addStrategy(LogStrategy strategy)
    {
        if (strategy != null && !this.strategies.contains(strategy))
        {
            this.strategies.add(strategy);
            return true;
        }
        return false;
    }

    /** Getter for the strategies held by this `Logger`.
     * 
     * Returns:
     *     ArrayList<LogStrategy>: The list of `LogStrategy` objects owned by the current `Logger`.
     */
    public ArrayList<LogStrategy> strategies()
    {
        return this.strategies;
    }

    protected void logImplementation(String text, HashMap<String, String> extraData)
    {
        /** Log the given text using the held strategies.
         * 
         * Args:
         *     text: The message to be logged by the different strategies.
         *     extraData: Keyword arguments containing info for the strategies to work as
         *         intended or to be forwarded to the mutators held by those strategies.
         */
        for (LogStrategy strategy : this.strategies)
        {
            strategy.log(text, extraData);
        }
    }

    private ArrayList<LogStrategy> strategies = new ArrayList<LogStrategy>();
}
