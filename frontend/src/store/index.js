import { create } from "zustand";
import { persist, createJSONStorage, devtools } from "zustand/middleware";
import { createCourseSlice } from "./slices/course.slice";
import { createUserSlice } from "./slices/user.slice";

export const useStore = create(
  devtools(
    persist(
      (...a) => ({
        ...createUserSlice(...a),
        ...createCourseSlice(...a),
      }),
      { name: "ntai-store", storage: createJSONStorage(() => sessionStorage) }
    ),
    { name: "NTAI Store" }
  )
);
