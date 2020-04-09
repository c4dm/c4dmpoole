title: Investigating Learning and Evaluation Methodologies for Music Language Modelling
-------------------------------------

<h2>
Adrien Ycart and Emmanouil Benetos - <i>IEEE TASLP 2020</i>
</h2>

<h3>
Presentation
</h3>


<p>
On this page can be found the supplementary material for:<br>
Adrien Ycart and Emmanouil Benetos.
  "Investigating Learning and Evaluation Methodologies for Music Language Modelling"
  <i>IEEE/ACM Transactions on Audio, Speech and Language Processing (TASLP), </i>
  Accepted, 2020.</li>
</p>

<h3>
Dataset splits
</h3>


<p>
The splits we used to reproduce the prediction experiments are available here: <a href=http://c4dm.eecs.qmul.ac.uk/datasets/ycart/taslp19/piano_midi_pred_split.zip> Piano-midi.de dataset split </a>
</p>

<h3>
Additional figures
</h3>

<h4>
Comparison of outputs with different models
</h4>



<figure>
    <img src="http://c4dm.eecs.qmul.ac.uk/datasets/ycart/taslp19/model_comparison.png" alt="Model comparison" width="100%" class="center" />
    <figcaption>Comparison of sigmoid outputs for various models for the MIDI file chpn-p7.mid transposed into C, with note-long (left) and note-short (right) timesteps.
    The ground truth notes are overlaid as red rectangles. The notes of the scale correspond to the white keys on the left of each image. The tonic is in grey. The same color map is used across images.</figcaption>
</figure>





<h4>
Grid search results with various timesteps
</h4>

<h5>
Table of results for AMT
</h5>


<figure>
    <img src="ycart/data/taslp19/table_AMT_full.pdf.png" alt="Results for AMT" width="100%" align="left" />
        Comparison of AMT performance for various MLMs. All results are obtained using the CW configuration, as described in <a href="http://archives.ismir.net/ismir2019/paper/000054.pdf">this paper</a>. The best values for each timestep are in bold.</figcaption>



<h5>
Visualisation - MLM evaluation
</h5>

<figure>
    <img src="ycart/data/taslp19/grid_search_40ms_MLM_title.pdf.png" alt="Grid search - MLM - 40ms" width="100%" class="center" />
    <figcaption>
    Evaluation of various MLMs trained with S loss, with various parameter configurations, all with 40ms timesteps. Brighter colours correspond to better performance (higher for F-measure, precision and recall, lower for cross-entropy-based metrics). 
    </figcaption>
</figure>
<figure>
    <img src="ycart/data/taslp19/grid_search_note_long_MLM_title.pdf.png" alt="Grid search - MLM - note-long" width="100%" class="center" />
    <figcaption>
    Evaluation of various MLMs trained with S loss, with various parameter configurations, all with note-long timesteps. Brighter colours correspond to better performance (higher for F-measure, precision and recall, lower for cross-entropy-based metrics). 
    </figcaption>
</figure>
<figure>
    <img src="ycart/data/taslp19/grid_search_note_short_MLM_title.pdf.png" alt="Grid search - MLM - note-short" width="100%" class="center" />
    <figcaption>
    Evaluation of various MLMs trained with S loss, with various parameter configurations, all with note-short timesteps. Brighter colours correspond to better performance (higher for F-measure, precision and recall, lower for cross-entropy-based metrics). 
    </figcaption>
</figure>



<h5>
Visualisation - AMT evaluation
</h5>

<figure>
    <img src="ycart/data/taslp19/grid_search_40ms_AMT_title.pdf.png" alt="Grid search - AMT - 40ms" width="100%" class="center" />
    <figcaption>
AMT performance of various MLMs trained with S loss, with various parameter configurations, all with 40ms timesteps. Brighter colours correspond to better values.
    </figcaption>
</figure>
<figure>
    <img src="ycart/data/taslp19/grid_search_note_long_AMT_title.pdf.png" alt="Grid search - AMT - note-long" width="100%" class="center" />
    <figcaption>
AMT performance of various MLMs trained with S loss, with various parameter configurations, all with note-long (16th note) timesteps. Brighter colours correspond to better values.
    </figcaption>
</figure>
<figure>
    <img src="ycart/data/taslp19/grid_search_note_short_AMT_title.pdf.png" alt="Grid search - AMT - note-short" width="100%" class="center" />
    <figcaption>
AMT performance of various MLMs trained with S loss, with various parameter configurations, all with note-short (48th note) timesteps. Brighter colours correspond to better values.
    </figcaption>
</figure>
