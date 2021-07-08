package ar.edu.ub.testing.logging;

import java.util.ArrayList;
import java.util.HashMap;

/** A base class to define the basics of a logging strategy.
 * 
 * These could actually be used without the need of a `Logger`.
 */
public abstract class LogStrategy
{
    /** Initialize the strategy.
     * 
     * Creates the internal lists to hold `Mutator`s and `Filter`s.
     */
    public LogStrategy()
    {
        this.mutators = new ArrayList<Mutator>();
        this.filters = new ArrayList<Filter>();
    }

    /** Method to be overriden by concrete classes.
     * 
     * Intended to do the actual logging with the message already mutated by the `Mutator`s. A
     * filtered message will not produce an invocation of this method.
     * Marked as protected/private because it shouldn't be called directly.
     * 
     * Args:
     *     text: The message to be logged.
     *     extraData: Keyword arguments that might contain data for the `LogStrategy` to
     *         work as intended.
     */
    protected abstract void logImplementation(String text, HashMap<String, String> extraData);

    /** Log the given message applying the internal `Mutator`s using the extra data.
     * 
     * Args:
     *     text: The message to be logged.
     *     extraData: Keyword arguments that might contain data for the `Mutator`s to
     *         work as intended. Note that each `Mutator` could have different requirements, so how
     *         the `extraData` is interpreted might vary.
     * 
     * Returns:
     *     bool: Confirmation whether the message has been logged or not (i.e. because it was
     *         filtered out).
     */
    public boolean log(String text, HashMap<String, String> extraData)
    {
        String mutatedMessage = this.mutate(text, extra_data);
        if (!this.filter(mutatedMessage, extraData))
        {
            this.logImplementation(mutatedMessage, extraData);
            return true;
        }
        return false;
    }

    /** Adds a `Mutator` to the current `LogStrategy`.
     *
     * Mutators will be applied to the messages to be logged prior to being logged.
     * Since one mutator can depend on the work of the previous one, the order matters.
     * 
     * Args:
     *     mutator: The `Mutator` to be added to this `LogStrategy`.
     * 
     * Returns:
     *     bool: Confirmation whether the mutator has been added to the mutators list or not.
     */
    public boolean addMutator(Mutator mutator)
    {
        if (mutator != null && !this.mutators.contains(mutator))
        {
            this.mutators.add(mutator);
            return true;
        }
        return false;
    }

    /** Removes a mutator from the list.
     * 
     * Args:
     *     mutator: A reference to the `Mutator` to remove from the list.
     * 
     * Returns:
     *     bool: Confirmation whether the mutator has been removed or not.
     */
    public boolean removeMutator(Mutator mutator)
    {
        if (mutator != null && this.mutators.contains(mutator))
        {
            this.mutators.remove(mutator);
            return true;
        }
        return false;
    }

    /** Returns the list of `Mutator`s applied in this `LogStrategy`.
     * 
     * Returns:
     *     ArrayList<Mutator>: The list of `Mutator`s the current `LogStrategy` holds.
     */
    public ArrayList<Mutator> mutators()
    {
        return this.mutators;
    }

    /** Clear all `Mutator`s from this `LogStrategy`. */
    public void clearMutators()
    {
        this.mutators.clear();
    }

    /** Add the given `Filter` to the current `LogStrategy` to filter messages.
     * 
     * Args:
     *     filter: The `Filter` to be added to this `LogStrategy`.
     * 
     * Returns:
     *     bool: Confirmation whether the filter has been added or not.
     */
    public boolean addFilter(Filter filter)
    {
        if (filter != null && !this.filters.contains(filter))
        {
            this.filters.add(filter);
            return true;
        }
        return false;
    }

    /** Removes the supplied `Filter` from this `LogStrategy`, if present.
     * 
     * Args:
     *     filter: The `Filter` to remove from the current `LogStrategy`.
     * 
     * Returns:
     *     bool: Confirmation whether the `Filter` was able to be removed or not (most likely
     *         because it was not there in the first place).
     */
    public boolean removeFilter(Filter filter)
    {
        if (this.filters.contains(filter))
        {
            this.filters.remove(filter);
            return true;
        }
        return false;
    }

    /** A getter for filters used by this `LogStrategy`.
     *
     *  Returns:
     *      list: A list of `Filter` objects the current `LogStrategy` is using.
     */
    public ArrayList<Filter> filters()
    {
        return this.filters;
    }

    /** Removes all filters this `LogStrategy` is using. */
    public void clearFilters()
    {
        this.filters.clear();
    }

    /** Apply all mutators to the incoming message.
     * 
     * Args:
     *     message: The message to mutate.
     *     extraData: HashMap containing data the `Mutator`s might need.
     * 
     * Returns:
     *     String: The mutated message.
     */
    protected String mutate(String text, HashMap<String, String> extraData)
    {
        String message = text;
        for (Mutator mutator : this.mutators)
        {
            message = mutator.mutate(message, extraData);
        }
        return message;
    }

    /** Apply filters to incoming messages.
     * 
     * Args:
     *     message: The message to check if it should be filtered out or not.
     *     extraData: Other parameters supplied along with the message aimed for the `Mutator`s
     *         and/or strategies, which could also be taken into account for message filtering.
     * 
     * Returns:
     *     boolean: `true` if the message should be filtered out, `false` otherwise.
     */
    protected boolean filter(String text, HashMap<String, String> extraData)
    {
        for (Filter filter : this.filters())
        {
            if (filter.filter(text, extraData))
            {
                return true;
            }
        }
        return false;
    }

    private ArrayList<Mutator> mutators;
    private ArrayList<Filter> filters;
}
