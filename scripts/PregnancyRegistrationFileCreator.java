package org.openconceptlab.idhack;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import com.google.gson.Gson;

/**
 * Represents a file containing a list of <code>PregnancyRegistration</code>s along with a string for metadata.
 * 
 * When executed, creates a JSON object.
 * 
 * @author jgreenberg
 *
 */
public class PregnancyRegistrationFileCreator {

	private List<PregnancyRegistration> all_registrations = new ArrayList<PregnancyRegistration>();
	private String metadata = "Notes here.";

	public List<PregnancyRegistration> getlPregReg() {
		return all_registrations;
	}

	public void setlPregReg(List<PregnancyRegistration> lPregReg) {
		this.all_registrations = lPregReg;
	}

	public String getsMetadata() {
		return metadata;
	}

	public void setsMetadata(String sMetadata) {
		this.metadata = sMetadata;
	}


	public static void main(String[] args) {
		PregnancyRegistrationFileCreator prdfc = new PregnancyRegistrationFileCreator();
		List<PregnancyRegistration> lPregReg = new ArrayList<PregnancyRegistration>();
		for (int i = 0; i < 100; i++) {
			lPregReg.add(new PregnancyRegistration(new Random().nextInt(9)));
		}
		prdfc.setlPregReg(lPregReg);
		Gson gson = new Gson();
		String strJson = gson.toJson(prdfc);

		System.out.println(strJson);
	}

}
