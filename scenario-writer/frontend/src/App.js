import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    icp_type: 'high_wage',
    milestone_code: 'M03',
    skill_target: '',
    language: 'en'
  });
  
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    setError(null);
    setResult(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!formData.skill_target.trim()) {
      setError('Please enter a skill target');
      return;
    }
    
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post('http://localhost:8000/generate-scenario', formData);
      
      if (response.data.success) {
        setResult(response.data.data);
      } else {
        setError(response.data.error);
      }
    } catch (err) {
      setError('Failed to connect to server. Make sure backend is running on port 8000');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <h1>AI Scenario Writer</h1>
        <p>Generate realistic workplace scenarios for any skill</p>
      </header>

      <div className="container">
        <div className="form-card">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>User Type</label>
              <div className="radio-group">
                <label className="radio-label">
                  <input
                    type="radio"
                    name="icp_type"
                    value="high_wage"
                    checked={formData.icp_type === 'high_wage'}
                    onChange={handleChange}
                  />
                  High Wage (Tech)
                </label>
                <label className="radio-label">
                  <input
                    type="radio"
                    name="icp_type"
                    value="low_wage"
                    checked={formData.icp_type === 'low_wage'}
                    onChange={handleChange}
                  />
                  Low Wage (Service)
                </label>
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Milestone</label>
                <select name="milestone_code" value={formData.milestone_code} onChange={handleChange}>
                  <option value="M01">M01 - Beginner</option>
                  <option value="M02">M02 - Developing</option>
                  <option value="M03">M03 - Intermediate</option>
                  <option value="M04">M04 - Proficient</option>
                  <option value="M05">M05 - Advanced</option>
                  <option value="M06">M06 - Expert</option>
                  <option value="M07">M07 - Master</option>
                </select>
              </div>

              <div className="form-group">
                <label>Language</label>
                <select name="language" value={formData.language} onChange={handleChange}>
                  <option value="en">English</option>
                  <option value="hi">हिंदी (Hindi)</option>
                </select>
              </div>
            </div>

            <div className="form-group">
              <label>Skill Target</label>
              <input
                type="text"
                name="skill_target"
                value={formData.skill_target}
                onChange={handleChange}
                placeholder="e.g., negotiation, customer service, leadership, time management"
                className="skill-input"
              />
            </div>

            <button type="submit" disabled={loading} className="generate-btn">
              {loading ? 'Generating...' : 'Generate Scenario'}
            </button>
          </form>
        </div>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {result && (
          <div className="result-card">
            <h2>Generated Scenario</h2>
            
            <div className="section">
              <h3>Scene</h3>
              <p><strong>Setting:</strong> {result.scene.setting}</p>
              <p><strong>Time:</strong> {result.scene.time}</p>
              <p><strong>Context:</strong> {result.scene.context}</p>
            </div>

            <div className="section">
              <h3>Characters</h3>
              <div className="characters">
                {result.characters.map((char, idx) => (
                  <div key={idx} className="character">
                    <span className="char-name">{char.name}</span>
                    <span className="char-role">({char.role})</span>
                    <span className="char-mood">- {char.mood}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="section">
              <h3>Antagonist Line</h3>
              <div className="antagonist-line">
                "{result.antagonist_opening_line}"
              </div>
            </div>

            <div className="section">
              <h3>Strategy Chips</h3>
              <div className="strategies">
                {result.strategy_chips.map((chip, idx) => (
                  <div key={idx} className="strategy">
                    <div className="strategy-label">{chip.label}</div>
                    <div className="strategy-philosophy">{chip.philosophy}</div>
                  </div>
                ))}
              </div>
            </div>

            <div className="section">
              <h3>Success Criteria</h3>
              <ul>
                {result.success_criteria.map((criteria, idx) => (
                  <li key={idx}>{criteria}</li>
                ))}
              </ul>
            </div>

            <div className="section">
              <h3>Rubric Scores</h3>
              <div className="rubric">
                <div className="rubric-item">
                  <span>Communication:</span>
                  <span className="score">{result.rubric.communication}</span>
                </div>
                <div className="rubric-item">
                  <span>Composure:</span>
                  <span className="score">{result.rubric.composure}</span>
                </div>
                <div className="rubric-item">
                  <span>Clarity:</span>
                  <span className="score">{result.rubric.clarity}</span>
                </div>
                <div className="rubric-item">
                  <span>Strategy:</span>
                  <span className="score">{result.rubric.strategy}</span>
                </div>
                <div className="rubric-item">
                  <span>Outcome:</span>
                  <span className="score">{result.rubric.outcome}</span>
                </div>
              </div>
            </div>

            <div className="section">
              <h3>Transfer Targets</h3>
              <div className="tags">
                {result.transfer_targets.map((target, idx) => (
                  <span key={idx} className="tag">{target}</span>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;