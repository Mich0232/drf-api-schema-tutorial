import { useEffect, useState } from 'react';
import { projectsList } from './api/endpoints/projects/projects.ts';
import { Project } from './api/endpoints/yourProjectAPI.schemas.ts';

function App() {
  const [projects, setProjects] = useState<Project[]>([]);

  useEffect(() => {
    async function fetchProjects() {
      const projects = await projectsList();
      if (projects.status === 200) {
        setProjects(projects.data);
      }
    }
    fetchProjects();
  }, []);

  return (
    <div>
      <ul>
        {projects.map((project) => (
          <li key={project.id}>{project.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
