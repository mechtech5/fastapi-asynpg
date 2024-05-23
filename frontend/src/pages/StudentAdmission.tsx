import { useState, ChangeEvent } from 'react';


const StudentAdmission = () => {
  const [studentForm, setStudentForm] = useState({})

  const onFormChange = (e: ChangeEvent<HTMLInputElement>, key: string) => {
    setStudentForm({ ...studentForm, [key]: e.target.value });
  }
  const handleSubmit = () => {
   
    console.log("Data", studentForm);
  };

  return (
    <>
      <form className="m-8" onSubmit={handleSubmit}>
        <div className="legal_name_contact_info">
          <div role="alert" className="alert">
            <span>Legal Name and Contact Information</span>
          </div>
          <div className="fname_lname flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">First Name</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legalfirstName')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Last Name</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legallastName')}
              />
            </label>
          </div>
          <div className="str_addr">
            <label className="form-control w-full">
              <div className="label">
                <span className="label-text-alt">Street Address</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legalstreetAddress')}
              />
            </label>
          </div>
          <div className="city_state_zip flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">City</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legalcity')}

              />
            </label>
            <label className="form-control w-full mx-1">
              <div className="label">
                <span className="label-text-alt">State / Province</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legalstate')}

              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Zip / Postal Code</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legalzipCode')}

              />
            </label>
          </div>
          <div className="country_home_cell flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">Country</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legalcountry')}

              />
            </label>
            <label className="form-control w-full mx-1">
              <div className="label">
                <span className="label-text-alt">Home phone</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legalhomePhone')}

              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Cell Phone</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legalcellPhone')}

              />
            </label>
          </div>
          <div className="email">
            <label className="form-control w-full">
              <div className="label">
                <span className="label-text-alt">Email</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legalemail')}
              />
            </label>
          </div>
          <div className="high-school-graduate flex items-center">
            <span className="label-text">High school Graduate</span>
            <div className="flex">
              <div className="form-control w-14">
                <label className="label cursor-pointer">
                  <span className="label-text-alt">Yes</span>
                  <input
                    type="radio"
                    name="radio-10"
                    className="radio checked:bg-green-500"
                    checked
                    onChange={(e) => onFormChange(e, 'legalyes')}
                  />
                </label>
              </div>
              <div className="form-control w-14">
                <label className="label cursor-pointer">
                  <span className="label-text-alt">No</span>
                  <input
                    type="radio"
                    name="radio-10"
                    className="radio checked:bg-red-500"
                    checked
                    onChange={(e) => onFormChange(e, 'legalno')}
                  />
                </label>
              </div>
            </div>
            <span className="label-text-alt">
              A minimum of a high school diploma/GED may be required for your
              course/program
            </span>
          </div>
          <div className="school_state_dates flex">
            <label className="form-control w-full mr-1">
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'legalschool')}
              />
              <div className="label flex justify-center">
                <span className="label-text-alt">School</span>
              </div>
            </label>
            <label className="form-control w-full mx-1">
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'highschoolstate')}
              />
              <div className="label justify-center">
                <span className="label-text-alt">State</span>
              </div>
            </label>
            <label className="form-control w-full ml-1">
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'datesAttended')}
              />
              <div className="label justify-center">
                <span className="label-text-alt">Dates Attended</span>
              </div>
            </label>
          </div>
        </div>
        
        <div className="citizenship">
          <div role="alert" className="alert">
            <span>Citizenship</span>
          </div>
          <div className="social_security_dob_gender flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">Social Security Number</span>
              </div>
              <input
                type="text"
                placeholder=""
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'citizenshipNumber')}
              />
            </label>
            <label className="form-control w-full mx-1">
              <div className="label">
                <span className="label-text-alt">DOB (mm/dd/yyyy)</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'citizenshipdob')}
              />
            </label>
            <div className="flex items-center w-full">
              <span className="label-text">Gender</span>
              <div className="flex">
                <div className="form-control w-14">
                  <label className="label cursor-pointer">
                    <input
                      type="radio"
                      name="radio-10"
                      className="radio checked:bg-green-500"
                      checked
                      onChange={(e) => onFormChange(e, 'citizenshipmale')}
                    />
                    <span className="label-text-alt">Male</span>
                  </label>
                </div>
                <div className="form-control w-14">
                  <label className="label cursor-pointer">
                    <input
                      type="radio"
                      name="radio-10"
                      className="radio checked:bg-red-500"
                      checked
                      onChange={(e) => onFormChange(e, 'citizenshipfemale')}
                    />
                    <span className="label-text-alt">Female</span>
                  </label>
                </div>
              </div>
            </div>
          </div>
          <div className="country_place flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">
                  Country of citizenship or Nationality
                </span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'citizenshipcountry')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Place of Birth</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'placeBirth')}
              />
            </label>
          </div>
          <div className="alien_number">
            <label className="form-control w-full">
              <div className="label">
                <span className="label-text-alt">Alien Number</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'alienNumber')}
              />
            </label>
          </div>
          <div className="native_language flex">
            <div className="w-full flex items-center">
              <span className="label-text">
                Is English your native language?
              </span>{" "}
              <div className="flex">
                <div className="form-control w-14">
                  <label className="label cursor-pointer">
                    <input
                      type="radio"
                      name="radio-10"
                      className="radio checked:bg-green-500"
                      checked
                      onChange={(e) => onFormChange(e, 'citizenshipyes')}
                    />
                    <span className="label-text-alt">Yes</span>
                  </label>
                </div>
                <div className="form-control w-14">
                  <label className="label cursor-pointer">
                    <input
                      type="radio"
                      name="radio-10"
                      className="radio checked:bg-red-500"
                      checked
                      onChange={(e) => onFormChange(e, 'citizenshipno')}
                    />
                    <span className="label-text-alt">No</span>
                  </label>
                </div>
              </div>
            </div>
            <label className="form-control w-full">
              <div className="label">
                <span className="label-text-alt">
                  What other languages do you speak?
                </span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'whatOther')}
              />
            </label>
          </div>
        </div>

        <div className="emergency mt-3">
          <div role="alert" className="alert">
            <span>Emergency Contact Information</span>
          </div>
          <div className="fname_lname flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">First Name</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencyfirstName')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Last Name</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencylastName')}
              />
            </label>
          </div>
          <div className="str_addr">
            <label className="form-control w-full">
              <div className="label">
                <span className="label-text-alt">Street Address</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencyAddress')}
              />
            </label>
          </div>
          <div className="city_state_zip flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">City</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencycity')}
              />
            </label>
            <label className="form-control w-full mx-1">
              <div className="label">
                <span className="label-text-alt">State / Province</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencystate')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Zip / Postal Code</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencyzipCode')}
              />
            </label>
          </div>
          <div className="country_home_cell flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">Country</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencycountry')}
              />
            </label>
            <label className="form-control w-full mx-1">
              <div className="label">
                <span className="label-text-alt">Home phone</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencyhomePhone')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Cell Phone</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencycellPhone')}
              />
            </label>
          </div>
          <div className="email-relationship flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">Email</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencyemail')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Relationship</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'emergencyrelationship')}
              />
            </label>
          </div>
          </div>

        <div className="work-experience mt-3">
          <div role="alert" className="alert">
            <span>Work Experience (Attach Resume)</span>
          </div>
          <div className="native_language flex">
            <div className="w-full flex items-center">
              <span className="label-text">
                Current Work Status:
              </span>{" "}
              <div className="flex space-x-14"> 
                <div className="form-control w-14">
                  <label className="label cursor-pointer">
                    <input type="radio" name="radio-10" className="radio checked:bg-green-500" checked                       
                    onChange={(e) => onFormChange(e, 'fullTime')}
                    />
                    <span className="label-text-alt">FullTime</span>
                  </label>
                </div>
                <div className="form-control w-14">
                  <label className="label cursor-pointer">
                    <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked                       
                    onChange={(e) => onFormChange(e, 'partTime')}
                    />
                    <span className="label-text-alt">PartTime</span>
                  </label>
                </div>
                <div className="form-control w-14">
                  <label className="label cursor-pointer">
                    <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked           
                    onChange={(e) => onFormChange(e, 'temporary')}
                    />
                    <span className="label-text-alt">Temporary</span>
                  </label>
                </div>
                <div className="form-control w-14">
                  <label className="label cursor-pointer">
                    <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked 
                    onChange={(e) => onFormChange(e, 'unemployed')}/>
                    <span className="label-text-alt">Unemployed</span>
                  </label>
                </div>
                <div className="form-control w-14">
                  <label className="label cursor-pointer">
                    <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked 
                    onChange={(e) => onFormChange(e, 'retired')}/>
                    <span className="label-text-alt">Retired</span>
                  </label>
                </div>
                <div className="form-control w-14">
                  <label className="label cursor-pointer">
                    <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked 
                    onChange={(e) => onFormChange(e, 'other')}/>
                    <span className="label-text-alt">Other</span>
                  </label>
                </div>
              </div>
            </div>
            <label className="form-control w-120">
              <div className="label">
                <span className="label-text-alt">
                  Other
                </span>
              </div>
              <input type="text" placeholder="Type here" className="input input-bordered w-120"                       
              onChange={(e) => onFormChange(e, 'other')}
              />
            </label>
          </div>
          </div>
          <div className="email-relationship flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">Most Recent Employer</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'mostRecent')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Position</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'position')}
              />
            </label>
          </div>
          <div className="dates-from flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">Dates Employed From</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'dateEmployed')}
              />
            </label>
            <label className="form-control w-full mx-1">
              <div className="label">
                <span className="label-text-alt">to</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'to')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Brief Description of Duties</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'briefDescription')}
              />
            </label>
          </div>


        <div className="work-experience mt-3">
          <div role="alert" className="alert">
            <span>Institutional</span>
          </div>
          <div className="alien_number">
            <label className="form-control w-full">
              <div className="label">
                <span className="label-text-alt">How did you hear about NTAi?</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'InstHow')}
              />
            </label>
          </div>
        </div>
        <div className="high_school_graduate flex items-center">
            <span className="label-text">Were you recommended by one of our students or employees?</span>{" "}
            <div className="flex">
              <div className="form-control w-14">
                <label className="label cursor-pointer">
                  <span className="label-text-alt">Yes</span>
                  <input
                    type="radio"
                    name="radio-10"
                    className="radio checked:bg-green-500"
                    checked
                    onChange={(e) => onFormChange(e, 'InstYes')}
                  />
                </label>
              </div>
              <div className="form-control w-14">
                <label className="label cursor-pointer">
                  <span className="label-text-alt">No</span>
                  <input
                    type="radio"
                    name="radio-10"
                    className="radio checked:bg-red-500"
                    checked
                    onChange={(e) => onFormChange(e, 'InstNo')}
                  />
                </label>
              </div>
            </div>
          </div>
          <div className="alien_number">
            <label className="form-control w-full">
              <div className="label">
                <span className="label-text-alt">If yes, whom</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'InstYes')}
              />
            </label>
          </div>
          <div className="high_school_graduate flex items-center">
            <span className="label-text">If sent by a state agency</span>
          </div>
          <div className="fname_lname flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">Name of Agency</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'nameagency')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Name of Counselor</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'namecounsellor')}
              />
            </label>
          </div>
          <div className="desired_name flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">Desired Start Date</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'desiredStart')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Courses you’re interested in</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'coursesYou')}
              />
            </label>
        </div>
        <div className="alien_number">
            <label className="form-control w-full">
              <div className="label">
                <span className="label-text-alt">List any and all certifications you have</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'InstAny')}
              />
            </label>

          <div className="high_school_graduate flex items-center">
          <span className="label-text">Do you know any friends that may be interested in NTAi’s training program? Please include their name and phone numbers</span>
          </div>
          <div className="fname_lname flex">
            <label className="form-control w-full mr-1">
              <div className="label">
                <span className="label-text-alt">Name</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'Instname')}
              />
            </label>
            <label className="form-control w-full ml-1">
              <div className="label">
                <span className="label-text-alt">Phone</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'Instphone')}
              />
            </label>
          </div>
          </div>

        <div className="survey mt-3">
          <div role="alert" className="alert">
            <span>Survey</span>
          </div>
          <div className="alien_number">
            <label className="form-control w-full">
              <div className="label">
                <span className="label-text-alt">Why do you want to enroll at NTAi?</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'whyDo')}
              />
            </label>
          </div>
          <div className="alien_number">
            <label className="form-control w-full">
              <div className="label">
                <span className="label-text-alt">What do you expect to get out of your time here?</span>
              </div>
              <input
                type="text"
                placeholder="Type here"
                className="input input-bordered w-full"
                onChange={(e) => onFormChange(e, 'whatDo')}
              />
            </label>
          </div>
          <span className="block mt-5">NTAi is a nondiscriminatory, equal opportunity institution, which admits students without regard to age, disability, race, ethnicity, religion, gender, sexual orientation, or national origin. Please check your primary ethnicity (Voluntary).</span>

          <div className="native_language flex">
          <div className="w-full flex items-center">
            <div className="flex space-x-16"> 
              <div className="form-control w-14">
                <label className="label cursor-pointer">
                  <input type="radio" name="radio-10" className="radio checked:bg-green-500" checked 
                  onChange={(e) => onFormChange(e, 'black')}/>
                  <span className="label-text-alt">Black</span>
                </label>
              </div>
              <div className="form-control w-14">
                <label className="label cursor-pointer">
                  <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked                       
                  onChange={(e) => onFormChange(e, 'white')}
                  />
                  <span className="label-text-alt">White</span>
                </label>
              </div>
              <div className="form-control w-14">
                <label className="label cursor-pointer">
                  <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked 
                  onChange={(e) => onFormChange(e, 'hispanic')}
                  />
                  <span className="label-text-alt">Hispanic</span>
                </label>
              </div>
              <div className="form-control w-14">
                <label className="label cursor-pointer">
                  <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked                       
                  onChange={(e) => onFormChange(e, 'american')}
                  />
                  <span className="label-text-alt">American Indian</span>
                </label>
              </div>
              <div className="form-control w-14">
                <label className="label cursor-pointer">
                  <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked 
                  onChange={(e) => onFormChange(e, 'asian')}
                  />
                  <span className="label-text-alt">Asian</span>
                </label>
              </div>
            </div>
          </div>
          <label className="form-control w-120">
            <div className="label">
              <span className="label-text-alt">
                Other
              </span>
            </div>
            <input type="text" placeholder="Type here" className="input input-bordered w-120"                       
            onChange={(e) => onFormChange(e, 'Surveyother')}
            />
          </label>
        </div>
        </div>
        <div className="flex justify-center">
        <button className="btn btn-active btn-accent" onSubmit={handleSubmit}>Submit</button>
      </div>
      </form>
      </>
  );
};

export default StudentAdmission;
