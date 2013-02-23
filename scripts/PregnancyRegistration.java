package org.openconceptlab.idhack;

/**
 * Represents a single registration of a user's pregnancy.
 * 
 * No two users may share the same unique ID.
 * 
 * @author jbhg
 *
 */
public class PregnancyRegistration {

	private static int NEXT_ID = 1;
	
	/**
	 * User's unique ID.
	 */
	private int nId;
	
	/**
	 * Dummy field.
	 */
	private int nWeeksToFirst;

	public PregnancyRegistration(int nWeeksToFirst)
	{
		nId = ++NEXT_ID;
		this.nWeeksToFirst = nWeeksToFirst;
	}
	
	public int getnId() { return nId; }

	public int getnWeeksToFirst() { return nWeeksToFirst; }
	
}
