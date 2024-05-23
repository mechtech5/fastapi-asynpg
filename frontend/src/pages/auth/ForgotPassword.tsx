import { useNavigate } from "react-router-dom";
import { useStore } from "../store";

const ForgotPassword = () => {
  const navigate = useNavigate();
  return (
    <div className="container mx-auto p-4 bg-slate-50">
      <div
        style={{ height: "80vh" }}
        className="flex justify-center items-center"
      >
        <div className="shadow-xl p-10 bg-white">
          <form>
            <div className="mb-4">
              <label className="input input-bordered flex items-center gap-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 16 16"
                  fill="currentColor"
                  className="w-4 h-4 opacity-70"
                >
                  <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" />
                </svg>
                <input type="text" className="grow" placeholder="Username" />
              </label>
            </div>

            <div className="text-center">
              <button className="btn btn-success text-white">Get Code</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default ForgotPassword;
