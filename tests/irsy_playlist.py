import sqlite3
import bs4

text = '''<div id="table-wrapper">
        <i>tip: use shift+mousewheel to scroll horizontally</i><br>
        <div id="table-scroll">
            <table class="pure-table pure-table-striped submissions-table">
                <thead>
                <tr>
                    <th class="center"><input type="checkbox" onclick="controlAllCheckboxes(this, 'submission-checkbox');"></th>
                    <th class="center">Files</th>
                    <th class="center">View</th>
                    <th class="center">Type</th>
                    <th>Title</th>
                    <th>18+</th>
                    
                    <th>Platform</th>
                    <th>Library</th>
                    <th>Level</th>
                    <th>Uploaded by</th>
                    <th>Updated by</th>
                    <th>Size</th>
                    <th>Bot</th>
                    <th class="bgr-assign-testing" title="Assigned for testing">AST</th>
                    <th class="bgr-request-changes" title="Requested Changes">RC</th>
                    <th class="bgr-approve" title="Approved">AP</th>
                    <th class="bgr-assign-verification" title="Assigned for verification">ASV</th>
                    <th class="bgr-verify" title="Verified">VE</th>
                    <th class="bgr-mark-added" title="Marked as added to Flashpoint">FP</th>
                    <th>Uploaded at</th>
                    <th>Updated at</th>
                    <th>Original Filename</th>
                </tr>
                </thead>
                <tbody>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77158" data-sid="64201">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64201/file/77158">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64201">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Alxemy</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="2016557B" id="submission-file-size-77158" data-size="2016557">
                            2.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-06 22:14:20 +0200</td>
                        <td>2023-05-06 22:14:57 +0200</td>
                        <td class="submission-table-original-filename">Alxemy.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77137" data-sid="64185">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64185/file/77137">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64185">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Rot Gut</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="6107039B" id="submission-file-size-77137" data-size="6107039">
                            6.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-06 10:05:45 +0200</td>
                        <td>2023-05-06 10:08:49 +0200</td>
                        <td class="submission-table-original-filename">Rot Gut.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77140" data-sid="64188">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64188/file/77140">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64188">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Bit Battles</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="6325848B" id="submission-file-size-77140" data-size="6325848">
                            6.3MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-06 10:06:35 +0200</td>
                        <td>2023-05-06 10:08:46 +0200</td>
                        <td class="submission-table-original-filename">Bit Battles.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77141" data-sid="64189">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64189/file/77141">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64189">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Bandido's Desert</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="13740452B" id="submission-file-size-77141" data-size="13740452">
                            13.7MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-06 10:06:55 +0200</td>
                        <td>2023-05-06 10:06:57 +0200</td>
                        <td class="submission-table-original-filename">Bandido's Desert.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77139" data-sid="64187">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64187/file/77139">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64187">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Urban Sumo</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="3346202B" id="submission-file-size-77139" data-size="3346202">
                            3.3MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-06 10:05:51 +0200</td>
                        <td>2023-05-06 10:05:53 +0200</td>
                        <td class="submission-table-original-filename">Urban Sumo.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77138" data-sid="64186">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64186/file/77138">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64186">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Tied Santa Escape</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="3809130B" id="submission-file-size-77138" data-size="3809130">
                            3.8MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-06 10:05:50 +0200</td>
                        <td>2023-05-06 10:05:52 +0200</td>
                        <td class="submission-table-original-filename">Tied Santa Escape.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77136" data-sid="64184">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64184/file/77136">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64184">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Gillette Revolution</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="4282002B" id="submission-file-size-77136" data-size="4282002">
                            4.3MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-06 10:05:26 +0200</td>
                        <td>2023-05-06 10:05:27 +0200</td>
                        <td class="submission-table-original-filename">Gillette Revolution.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77135" data-sid="64183">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64183/file/77135">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64183">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Flip World</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="190011B" id="submission-file-size-77135" data-size="190011">
                            190.0kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-06 10:05:02 +0200</td>
                        <td>2023-05-06 10:05:03 +0200</td>
                        <td class="submission-table-original-filename">Flip World.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77085" data-sid="64151">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64151/file/77085">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64151">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">A Game About Game Literacy</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="7151798B" id="submission-file-size-77085" data-size="7151798">
                            7.2MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-05 20:58:10 +0200</td>
                        <td>2023-05-05 20:58:31 +0200</td>
                        <td class="submission-table-original-filename">A Game About Game Literacy.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77084" data-sid="64150">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64150/file/77084">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64150">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Aliens Kidnapped Betty</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="1125791B" id="submission-file-size-77084" data-size="1125791">
                            1.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-05 20:57:43 +0200</td>
                        <td>2023-05-05 20:58:21 +0200</td>
                        <td class="submission-table-original-filename">Aliens Kidnapped Betty.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77072" data-sid="64138">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64138/file/77072">Get</a>
                                
                                    <br><a href="/web/submission/64138/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64138">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Onomastica 2</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="1636263B" id="submission-file-size-77072" data-size="1636263">
                            1.6MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-05 20:15:44 +0200</td>
                        <td>2023-05-05 20:21:43 +0200</td>
                        <td class="submission-table-original-filename">Onomastica 2.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77071" data-sid="64135">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64135/file/77071">Get</a>
                                
                                    <br><a href="/web/submission/64135/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64135">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Ledge the Spirit Stone</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="2105465B" id="submission-file-size-77071" data-size="2105465">
                            2.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-05 20:15:22 +0200</td>
                        <td>2023-05-05 20:21:36 +0200</td>
                        <td class="submission-table-original-filename">Ledge the Spirit Stone.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77070" data-sid="64133">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64133/file/77070">Get</a>
                                
                                    <br><a href="/web/submission/64133/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64133">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Billy Bob Abduction</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>irsY</td>
                        <td class="right" title="818295B" id="submission-file-size-77070" data-size="818295">
                            818.3kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-05 20:14:51 +0200</td>
                        <td>2023-05-05 20:20:34 +0200</td>
                        <td class="submission-table-original-filename">Billy Bob Abduction.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77068" data-sid="64137">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64137/file/77068">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64137">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Onomastica</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="728984B" id="submission-file-size-77068" data-size="728984">
                            729.0kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-05 20:15:37 +0200</td>
                        <td>2023-05-05 20:18:01 +0200</td>
                        <td class="submission-table-original-filename">Onomastica.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77067" data-sid="64136">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64136/file/77067">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64136">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Minx's Cake Decoration</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="1010337B" id="submission-file-size-77067" data-size="1010337">
                            1.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-05 20:15:23 +0200</td>
                        <td>2023-05-05 20:17:43 +0200</td>
                        <td class="submission-table-original-filename">Minx's Cake Decoration.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77065" data-sid="64134">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64134/file/77065">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64134">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Make-a-Scene Jinx &amp; Minx at the Beach</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="282660B" id="submission-file-size-77065" data-size="282660">
                            282.7kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-05 20:15:00 +0200</td>
                        <td>2023-05-05 20:17:40 +0200</td>
                        <td class="submission-table-original-filename">Make-a-Scene Jinx &amp; Minx at the Beach.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77063" data-sid="64132">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64132/file/77063">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64132">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">1 on 1 Soccer</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="322797B" id="submission-file-size-77063" data-size="322797">
                            322.8kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-05 20:13:59 +0200</td>
                        <td>2023-05-05 20:17:29 +0200</td>
                        <td class="submission-table-original-filename">1 on 1 Soccer.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="77061" data-sid="64130">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/64130/file/77061">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/64130">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/puzzle-piece.svg" alt="Content Change">
                            
                        </td>
                        <td class="submission-table-title">Glassez!</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="336995B" id="submission-file-size-77061" data-size="336995">
                            337.0kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-05-05 19:37:32 +0200</td>
                        <td>2023-05-05 19:38:28 +0200</td>
                        <td class="submission-table-original-filename">Glassez!.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="76685" data-sid="63618">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/63618/file/76685">Get</a>
                                
                                    <br><a href="/web/submission/63618/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/63618">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Into the Wild</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="6794215B" id="submission-file-size-76685" data-size="6794215">
                            6.8MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-04-24 16:40:45 +0200</td>
                        <td>2023-04-30 10:45:26 +0200</td>
                        <td class="submission-table-original-filename">Into the Wild.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="76684" data-sid="63832">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/63832/file/76684">Get</a>
                                
                                    <br><a href="/web/submission/63832/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/63832">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Gorilla Cop</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="4518636B" id="submission-file-size-76684" data-size="4518636">
                            4.5MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-04-30 09:43:46 +0200</td>
                        <td>2023-04-30 09:46:47 +0200</td>
                        <td class="submission-table-original-filename">Gorilla Cop.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="76683" data-sid="63834">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/63834/file/76683">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/63834">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Air Guitar Tutor</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="5217669B" id="submission-file-size-76683" data-size="5217669">
                            5.2MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-04-30 09:43:48 +0200</td>
                        <td>2023-04-30 09:43:50 +0200</td>
                        <td class="submission-table-original-filename">Air Guitar Tutor.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="76682" data-sid="63833">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/63833/file/76682">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/63833">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Trolley Racer</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="1896637B" id="submission-file-size-76682" data-size="1896637">
                            1.9MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-04-30 09:43:47 +0200</td>
                        <td>2023-04-30 09:43:48 +0200</td>
                        <td class="submission-table-original-filename">Trolley Racer.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="76680" data-sid="63831">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/63831/file/76680">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/63831">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Elf Chimney Seeker</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="2142352B" id="submission-file-size-76680" data-size="2142352">
                            2.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-04-30 09:43:38 +0200</td>
                        <td>2023-04-30 09:43:39 +0200</td>
                        <td class="submission-table-original-filename">Elf Chimney Seeker.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="76415" data-sid="63657">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/63657/file/76415">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/63657">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Water Blaster</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>RedMinima</td>
                        <td class="right" title="977367B" id="submission-file-size-76415" data-size="977367">
                            977.4kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-comment" title="Not marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-04-25 12:09:28 +0200</td>
                        <td>2023-04-25 12:09:30 +0200</td>
                        <td class="submission-table-original-filename">Water Blaster.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="74165" data-sid="62099">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/62099/file/74165">Get</a>
                                
                                    <br><a href="/web/submission/62099/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/62099">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Trolleez</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="2146888B" id="submission-file-size-74165" data-size="2146888">
                            2.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-03-17 18:44:32 +0100</td>
                        <td>2023-04-25 10:55:43 +0200</td>
                        <td class="submission-table-original-filename">Trolleez.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="73832" data-sid="61830">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/61830/file/73832">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/61830">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">DD Finger Skate Park Game</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="3540978B" id="submission-file-size-73832" data-size="3540978">
                            3.5MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-03-10 19:42:20 +0100</td>
                        <td>2023-04-25 10:54:00 +0200</td>
                        <td class="submission-table-original-filename">DD Finger Skate Park Game.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="73837" data-sid="61835">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/61835/file/73837">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/61835">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Una Notte da Supereroe</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="3431146B" id="submission-file-size-73837" data-size="3431146">
                            3.4MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-03-10 19:42:32 +0100</td>
                        <td>2023-04-25 10:53:59 +0200</td>
                        <td class="submission-table-original-filename">Una Notte da Supereroe.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="75893" data-sid="61831">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/61831/file/75893">Get</a>
                                
                                    <br><a href="/web/submission/61831/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/61831">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Armadillo Adventure</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="4346419B" id="submission-file-size-75893" data-size="4346419">
                            4.3MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-03-10 19:42:22 +0100</td>
                        <td>2023-04-25 10:53:58 +0200</td>
                        <td class="submission-table-original-filename">Armadillo Adventure.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="73834" data-sid="61832">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/61832/file/73834">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/61832">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Il Memory di Paperino</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="2121861B" id="submission-file-size-73834" data-size="2121861">
                            2.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-03-10 19:42:27 +0100</td>
                        <td>2023-04-25 10:53:52 +0200</td>
                        <td class="submission-table-original-filename">Il Memory di Paperino.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="73835" data-sid="61833">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/61833/file/73835">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/61833">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">DD Hacker Attack</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="5744050B" id="submission-file-size-73835" data-size="5744050">
                            5.7MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-03-10 19:42:30 +0100</td>
                        <td>2023-04-25 10:53:52 +0200</td>
                        <td class="submission-table-original-filename">DD Hacker Attack.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="73836" data-sid="61834">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/61834/file/73836">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/61834">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Operazione Elicottero - Fermate Macchia Nera!</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="1159606B" id="submission-file-size-73836" data-size="1159606">
                            1.2MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-03-10 19:42:31 +0100</td>
                        <td>2023-04-25 10:53:52 +0200</td>
                        <td class="submission-table-original-filename">Operazione Elicottero - Fermate Macchia Nera!.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="73735" data-sid="61763">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/61763/file/73735">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/61763">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">L'Eredità</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="3673299B" id="submission-file-size-73735" data-size="3673299">
                            3.7MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-03-08 21:10:47 +0100</td>
                        <td>2023-04-24 20:41:18 +0200</td>
                        <td class="submission-table-original-filename">L'Eredità.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="73734" data-sid="61762">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/61762/file/73734">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/61762">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Il gioco dei pacchi</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Staff</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="390988B" id="submission-file-size-73734" data-size="390988">
                            391.0kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-03-08 21:10:04 +0100</td>
                        <td>2023-04-24 20:41:17 +0200</td>
                        <td class="submission-table-original-filename">Il gioco dei pacchi.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70844" data-sid="59246">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/59246/file/70844">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/59246">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Monster's Lawn</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="2902258B" id="submission-file-size-70844" data-size="2902258">
                            2.9MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-29 07:36:43 +0100</td>
                        <td>2023-03-19 11:21:40 +0100</td>
                        <td class="submission-table-original-filename">Monster's Lawn.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71008" data-sid="58995">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58995/file/71008">Get</a>
                                
                                    <br><a href="/web/submission/58995/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58995">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Steel Head</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="2669248B" id="submission-file-size-71008" data-size="2669248">
                            2.7MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:29:02 +0100</td>
                        <td>2023-03-19 11:21:14 +0100</td>
                        <td class="submission-table-original-filename">Steel Head.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70580" data-sid="58998">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58998/file/70580">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58998">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">The Tuttles - Madcap Misadventures</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="6623865B" id="submission-file-size-70580" data-size="6623865">
                            6.6MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:29:11 +0100</td>
                        <td>2023-03-19 11:21:14 +0100</td>
                        <td class="submission-table-original-filename">The Tuttles - Madcap Misadventures.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70570" data-sid="58988">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58988/file/70570">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58988">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Polleke's Garden Escape</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="326594B" id="submission-file-size-70570" data-size="326594">
                            326.6kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:53 +0100</td>
                        <td>2023-03-19 11:21:13 +0100</td>
                        <td class="submission-table-original-filename">Polleke's Garden Escape.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71007" data-sid="58994">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58994/file/71007">Get</a>
                                
                                    <br><a href="/web/submission/58994/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58994">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">SnowLemmings</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="3254342B" id="submission-file-size-71007" data-size="3254342">
                            3.3MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:29:01 +0100</td>
                        <td>2023-03-19 11:21:13 +0100</td>
                        <td class="submission-table-original-filename">SnowLemmings.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71009" data-sid="58997">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58997/file/71009">Get</a>
                                
                                    <br><a href="/web/submission/58997/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58997">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Zombies Runaway</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="5167181B" id="submission-file-size-71009" data-size="5167181">
                            5.2MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:29:10 +0100</td>
                        <td>2023-03-19 11:21:13 +0100</td>
                        <td class="submission-table-original-filename">Zombies Runaway.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71210" data-sid="58986">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58986/file/71210">Get</a>
                                
                                    <br><a href="/web/submission/58986/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58986">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Oh My Bot</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="1964087B" id="submission-file-size-71210" data-size="1964087">
                            2.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:51 +0100</td>
                        <td>2023-03-19 11:21:12 +0100</td>
                        <td class="submission-table-original-filename">Oh My Bot.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70569" data-sid="58987">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58987/file/70569">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58987">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Noah the Karateka</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="7014722B" id="submission-file-size-70569" data-size="7014722">
                            7.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:52 +0100</td>
                        <td>2023-03-19 11:21:12 +0100</td>
                        <td class="submission-table-original-filename">Noah the Karateka.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70571" data-sid="58989">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58989/file/70571">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58989">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Polleke's Room Escape</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="229437B" id="submission-file-size-70571" data-size="229437">
                            229.4kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:54 +0100</td>
                        <td>2023-03-19 11:21:12 +0100</td>
                        <td class="submission-table-original-filename">Polleke's Room Escape.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70573" data-sid="58991">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58991/file/70573">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58991">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Polleke's Room part II</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="226444B" id="submission-file-size-70573" data-size="226444">
                            226.4kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:56 +0100</td>
                        <td>2023-03-19 11:21:12 +0100</td>
                        <td class="submission-table-original-filename">Polleke's Room part II.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70574" data-sid="58992">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58992/file/70574">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58992">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Santa's Gifts</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="925827B" id="submission-file-size-70574" data-size="925827">
                            925.8kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:57 +0100</td>
                        <td>2023-03-19 11:21:12 +0100</td>
                        <td class="submission-table-original-filename">Santa's Gifts.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70575" data-sid="58993">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58993/file/70575">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58993">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Princess Bride Game - Fire Swamp</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="4929939B" id="submission-file-size-70575" data-size="4929939">
                            4.9MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:59 +0100</td>
                        <td>2023-03-19 11:21:12 +0100</td>
                        <td class="submission-table-original-filename">Princess Bride Game - Fire Swamp.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71010" data-sid="58996">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58996/file/71010">Get</a>
                                
                                    <br><a href="/web/submission/58996/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58996">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">The Escape Game of Bird's-Eye View</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="509846B" id="submission-file-size-71010" data-size="509846">
                            509.8kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:29:03 +0100</td>
                        <td>2023-03-19 11:21:12 +0100</td>
                        <td class="submission-table-original-filename">The Escape Game of Bird's-Eye View.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70566" data-sid="58984">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58984/file/70566">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58984">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Lapinka Oak Adventure</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="1728820B" id="submission-file-size-70566" data-size="1728820">
                            1.7MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:47 +0100</td>
                        <td>2023-03-19 11:21:11 +0100</td>
                        <td class="submission-table-original-filename">Lapinka Oak Adventure.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70572" data-sid="58990">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58990/file/70572">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58990">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Parkour Parkour</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="4634298B" id="submission-file-size-70572" data-size="4634298">
                            4.6MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:55 +0100</td>
                        <td>2023-03-19 11:21:11 +0100</td>
                        <td class="submission-table-original-filename">Parkour Parkour.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70559" data-sid="58977">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58977/file/70559">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58977">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Flying Monkey</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="730890B" id="submission-file-size-70559" data-size="730890">
                            730.9kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:33 +0100</td>
                        <td>2023-03-19 11:21:10 +0100</td>
                        <td class="submission-table-original-filename">Flying Monkey.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70560" data-sid="58978">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58978/file/70560">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58978">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">flowEST</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="4589430B" id="submission-file-size-70560" data-size="4589430">
                            4.6MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:35 +0100</td>
                        <td>2023-03-19 11:21:10 +0100</td>
                        <td class="submission-table-original-filename">flowEST.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70561" data-sid="58979">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58979/file/70561">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58979">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Gray</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="2677896B" id="submission-file-size-70561" data-size="2677896">
                            2.7MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:37 +0100</td>
                        <td>2023-03-19 11:21:10 +0100</td>
                        <td class="submission-table-original-filename">Gray.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71200" data-sid="58981">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58981/file/71200">Get</a>
                                
                                    <br><a href="/web/submission/58981/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58981">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Jumpz</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="2173765B" id="submission-file-size-71200" data-size="2173765">
                            2.2MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:41 +0100</td>
                        <td>2023-03-19 11:21:10 +0100</td>
                        <td class="submission-table-original-filename">Jumpz.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70565" data-sid="58983">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58983/file/70565">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58983">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Just John</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="1091289B" id="submission-file-size-70565" data-size="1091289">
                            1.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:46 +0100</td>
                        <td>2023-03-19 11:21:10 +0100</td>
                        <td class="submission-table-original-filename">Just John.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70567" data-sid="58985">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58985/file/70567">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58985">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Octopussie Escape</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="620889B" id="submission-file-size-70567" data-size="620889">
                            620.9kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:48 +0100</td>
                        <td>2023-03-19 11:21:10 +0100</td>
                        <td class="submission-table-original-filename">Octopussie Escape.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70550" data-sid="58968">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58968/file/70550">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58968">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Bank Robbery</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="795360B" id="submission-file-size-70550" data-size="795360">
                            795.4kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:17 +0100</td>
                        <td>2023-03-19 11:21:09 +0100</td>
                        <td class="submission-table-original-filename">Bank Robbery.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71214" data-sid="58970">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58970/file/71214">Get</a>
                                
                                    <br><a href="/web/submission/58970/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58970">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Battle Ram</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="3452268B" id="submission-file-size-71214" data-size="3452268">
                            3.5MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:21 +0100</td>
                        <td>2023-03-19 11:21:09 +0100</td>
                        <td class="submission-table-original-filename">Battle Ram.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70553" data-sid="58971">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58971/file/70553">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58971">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">D's Find Petals</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="396059B" id="submission-file-size-70553" data-size="396059">
                            396.1kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:22 +0100</td>
                        <td>2023-03-19 11:21:09 +0100</td>
                        <td class="submission-table-original-filename">D's Find Petals.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70555" data-sid="58973">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58973/file/70555">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58973">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Egypt Explore</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="1314554B" id="submission-file-size-70555" data-size="1314554">
                            1.3MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:27 +0100</td>
                        <td>2023-03-19 11:21:09 +0100</td>
                        <td class="submission-table-original-filename">Egypt Explore.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70556" data-sid="58974">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58974/file/70556">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58974">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Escape From The Cube</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="1041830B" id="submission-file-size-70556" data-size="1041830">
                            1.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:30 +0100</td>
                        <td>2023-03-19 11:21:09 +0100</td>
                        <td class="submission-table-original-filename">Escape From The Cube.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71203" data-sid="58975">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58975/file/71203">Get</a>
                                
                                    <br><a href="/web/submission/58975/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58975">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Daily Battle - The Mystery of Ixtab</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="7148940B" id="submission-file-size-71203" data-size="7148940">
                            7.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:31 +0100</td>
                        <td>2023-03-19 11:21:09 +0100</td>
                        <td class="submission-table-original-filename">Daily Battle - The Mystery of Ixtab.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70558" data-sid="58976">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58976/file/70558">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58976">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Escape the Lab</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="1171477B" id="submission-file-size-70558" data-size="1171477">
                            1.2MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:32 +0100</td>
                        <td>2023-03-19 11:21:09 +0100</td>
                        <td class="submission-table-original-filename">Escape the Lab.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70562" data-sid="58980">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58980/file/70562">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58980">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">IceCube</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="945213B" id="submission-file-size-70562" data-size="945213">
                            945.2kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:38 +0100</td>
                        <td>2023-03-19 11:21:09 +0100</td>
                        <td class="submission-table-original-filename">IceCube.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70551" data-sid="58969">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58969/file/70551">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58969">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Alien Attack</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="536338B" id="submission-file-size-70551" data-size="536338">
                            536.3kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:18 +0100</td>
                        <td>2023-03-19 11:21:08 +0100</td>
                        <td class="submission-table-original-filename">Alien Attack.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70554" data-sid="58972">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58972/file/70554">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58972">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Cyber Nibblet</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="2690822B" id="submission-file-size-70554" data-size="2690822">
                            2.7MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-25 18:28:24 +0100</td>
                        <td>2023-03-19 11:21:07 +0100</td>
                        <td class="submission-table-original-filename">Cyber Nibblet.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70139" data-sid="58589">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58589/file/70139">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58589">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">White Jumping</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="1868609B" id="submission-file-size-70139" data-size="1868609">
                            1.9MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-21 21:58:31 +0100</td>
                        <td>2023-03-18 20:11:48 +0100</td>
                        <td class="submission-table-original-filename">White Jumping.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71202" data-sid="58585">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58585/file/71202">Get</a>
                                
                                    <br><a href="/web/submission/58585/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58585">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Moon &amp; Sun</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="2025659B" id="submission-file-size-71202" data-size="2025659">
                            2.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-21 20:50:35 +0100</td>
                        <td>2023-03-18 20:11:47 +0100</td>
                        <td class="submission-table-original-filename">Moon &amp; Sun.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70076" data-sid="58532">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58532/file/70076">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58532">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Miami Outlaws</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="4674255B" id="submission-file-size-70076" data-size="4674255">
                            4.7MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-21 14:33:57 +0100</td>
                        <td>2023-03-18 20:11:38 +0100</td>
                        <td class="submission-table-original-filename">Miami Outlaws.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="73023" data-sid="58533">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58533/file/73023">Get</a>
                                
                                    <br><a href="/web/submission/58533/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58533">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Epic Attack</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="7094630B" id="submission-file-size-73023" data-size="7094630">
                            7.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-21 14:34:01 +0100</td>
                        <td>2023-03-18 20:11:38 +0100</td>
                        <td class="submission-table-original-filename">Epic Attack.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="70075" data-sid="58531">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58531/file/70075">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58531">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">ACR Bumper Cars Championship</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="1535882B" id="submission-file-size-70075" data-size="1535882">
                            1.5MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-21 14:33:20 +0100</td>
                        <td>2023-03-18 20:11:37 +0100</td>
                        <td class="submission-table-original-filename">ACR Bumper Cars Championship.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="69939" data-sid="58412">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58412/file/69939">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58412">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Spying Around</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="4248832B" id="submission-file-size-69939" data-size="4248832">
                            4.2MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-20 10:15:01 +0100</td>
                        <td>2023-03-18 20:11:22 +0100</td>
                        <td class="submission-table-original-filename">Spying Around.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="69940" data-sid="58413">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58413/file/69940">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58413">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">My Spiderman</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="341633B" id="submission-file-size-69940" data-size="341633">
                            341.6kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-20 10:15:06 +0100</td>
                        <td>2023-03-18 20:11:22 +0100</td>
                        <td class="submission-table-original-filename">My Spiderman.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="69901" data-sid="58375">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58375/file/69901">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58375">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Fruits World Party</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="6871385B" id="submission-file-size-69901" data-size="6871385">
                            6.9MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-19 22:16:27 +0100</td>
                        <td>2023-03-18 20:11:18 +0100</td>
                        <td class="submission-table-original-filename">Fruits World Party.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71205" data-sid="58363">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58363/file/71205">Get</a>
                                
                                    <br><a href="/web/submission/58363/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58363">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Paper Snail</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>Colin</td>
                        <td class="right" title="6996293B" id="submission-file-size-71205" data-size="6996293">
                            7.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2023-01-19 21:32:49 +0100</td>
                        <td>2023-03-18 20:11:16 +0100</td>
                        <td class="submission-table-original-filename">Paper Snail.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="71211" data-sid="58982">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/58982/file/71211">Get</a>
                                
                                    <br><a href="/web/submission/58982/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/58982">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">It's Dark in Hell</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>irsY</td>
                        <td class="right" title="4707440B" id="submission-file-size-71211" data-size="4707440">
                            4.7MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-reject" title="Rejected."></div>
                        </td>
                        <td>2023-01-25 18:28:45 +0100</td>
                        <td>2023-02-01 16:34:02 +0100</td>
                        <td class="submission-table-original-filename">It's Dark in Hell.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="67236" data-sid="53313">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/53313/file/67236">Get</a>
                                
                                    <br><a href="/web/submission/53313/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/53313">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Time Machine 2: Medieval Cooking</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="4001749B" id="submission-file-size-67236" data-size="4001749">
                            4.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-12-02 23:16:51 +0100</td>
                        <td>2022-12-26 02:32:05 +0100</td>
                        <td class="submission-table-original-filename">Time Machine 2 Medieval Cooking.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="63759" data-sid="53314">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/53314/file/63759">Get</a>
                                
                                    <br><a href="/web/submission/53314/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/53314">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Time Machine 3: Futuristic Cooking</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="3621035B" id="submission-file-size-63759" data-size="3621035">
                            3.6MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-12-02 23:16:56 +0100</td>
                        <td>2022-12-24 01:51:27 +0100</td>
                        <td class="submission-table-original-filename">Time Machine 3 Futuristic Cooking.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="63755" data-sid="53312">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/53312/file/63755">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/53312">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Butterfly Coloring</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="407936B" id="submission-file-size-63755" data-size="407936">
                            407.9kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-12-02 23:16:39 +0100</td>
                        <td>2022-12-24 01:51:22 +0100</td>
                        <td class="submission-table-original-filename">Butterfly Coloring.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="54045" data-sid="44855">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44855/file/54045">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44855">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">War of the GoBots</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="296507B" id="submission-file-size-54045" data-size="296507">
                            296.5kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-25 15:46:32 +0200</td>
                        <td>2022-10-02 10:09:14 +0200</td>
                        <td class="submission-table-original-filename">War of the GoBots.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="54046" data-sid="44856">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44856/file/54046">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44856">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Super Robot Action Game</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="2505164B" id="submission-file-size-54046" data-size="2505164">
                            2.5MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-25 15:49:24 +0200</td>
                        <td>2022-10-02 10:09:14 +0200</td>
                        <td class="submission-table-original-filename">Super Robot Action Game.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53978" data-sid="44797">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44797/file/53978">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44797">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Little Locations</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="871459B" id="submission-file-size-53978" data-size="871459">
                            871.5kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:18:42 +0200</td>
                        <td>2022-10-02 10:08:58 +0200</td>
                        <td class="submission-table-original-filename">Little Locations.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53979" data-sid="44798">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44798/file/53979">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44798">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Christmas Cookie Chase</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="2318778B" id="submission-file-size-53979" data-size="2318778">
                            2.3MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:19:18 +0200</td>
                        <td>2022-10-02 10:08:58 +0200</td>
                        <td class="submission-table-original-filename">Christmas Cookie Chase.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53970" data-sid="44789">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44789/file/53970">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44789">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Space Battle 2P</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="2172542B" id="submission-file-size-53970" data-size="2172542">
                            2.2MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:33 +0200</td>
                        <td>2022-10-02 10:08:57 +0200</td>
                        <td class="submission-table-original-filename">Space Battle 2P.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53976" data-sid="44795">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44795/file/53976">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44795">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Menu Screen: The Game</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="2959645B" id="submission-file-size-53976" data-size="2959645">
                            3.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:18:08 +0200</td>
                        <td>2022-10-02 10:08:57 +0200</td>
                        <td class="submission-table-original-filename">Menu Screen The Game.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53977" data-sid="44796">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44796/file/53977">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44796">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Mouse Adventures</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="37141B" id="submission-file-size-53977" data-size="37141">
                            37.1kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:18:08 +0200</td>
                        <td>2022-10-02 10:08:57 +0200</td>
                        <td class="submission-table-original-filename">Mouse Adventures.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53969" data-sid="44788">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44788/file/53969">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44788">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Super BroBalls</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="2542594B" id="submission-file-size-53969" data-size="2542594">
                            2.5MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:32 +0200</td>
                        <td>2022-10-02 10:08:56 +0200</td>
                        <td class="submission-table-original-filename">Super BroBalls.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53972" data-sid="44791">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44791/file/53972">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44791">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Back to Cool</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="3301119B" id="submission-file-size-53972" data-size="3301119">
                            3.3MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:34 +0200</td>
                        <td>2022-10-02 10:08:56 +0200</td>
                        <td class="submission-table-original-filename">Back to Cool.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53973" data-sid="44792">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44792/file/53973">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44792">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">SpaceBox</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="1986485B" id="submission-file-size-53973" data-size="1986485">
                            2.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:34 +0200</td>
                        <td>2022-10-02 10:08:56 +0200</td>
                        <td class="submission-table-original-filename">SpaceBox.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53974" data-sid="44793">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44793/file/53974">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44793">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Adapt1</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="4999625B" id="submission-file-size-53974" data-size="4999625">
                            5.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:58 +0200</td>
                        <td>2022-10-02 10:08:56 +0200</td>
                        <td class="submission-table-original-filename">Adapt1.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53975" data-sid="44794">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44794/file/53975">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44794">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Level10</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="252431B" id="submission-file-size-53975" data-size="252431">
                            252.4kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:18:07 +0200</td>
                        <td>2022-10-02 10:08:56 +0200</td>
                        <td class="submission-table-original-filename">Level10.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53965" data-sid="44784">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44784/file/53965">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44784">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Vectricity</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="238023B" id="submission-file-size-53965" data-size="238023">
                            238.0kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:30 +0200</td>
                        <td>2022-10-02 10:08:55 +0200</td>
                        <td class="submission-table-original-filename">Vectricity.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53966" data-sid="44785">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44785/file/53966">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44785">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Ereban Dawn</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="916960B" id="submission-file-size-53966" data-size="916960">
                            917.0kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:30 +0200</td>
                        <td>2022-10-02 10:08:55 +0200</td>
                        <td class="submission-table-original-filename">Ereban Dawn.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="56364" data-sid="44787">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44787/file/56364">Get</a>
                                
                                    <br><a href="/web/submission/44787/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44787">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">The Unbeatable Path</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="4436163B" id="submission-file-size-56364" data-size="4436163">
                            4.4MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:31 +0200</td>
                        <td>2022-10-02 10:08:55 +0200</td>
                        <td class="submission-table-original-filename">The Unbeatable Path.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53961" data-sid="44780">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44780/file/53961">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44780">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Shakespeare Authorship Controversy: The Video Game</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="1415852B" id="submission-file-size-53961" data-size="1415852">
                            1.4MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:27 +0200</td>
                        <td>2022-10-02 10:08:54 +0200</td>
                        <td class="submission-table-original-filename">Shakespeare Authorship Controversy The Video Game.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="56363" data-sid="44782">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44782/file/56363">Get</a>
                                
                                    <br><a href="/web/submission/44782/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44782">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Perilous Presents</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="2573235B" id="submission-file-size-56363" data-size="2573235">
                            2.6MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:28 +0200</td>
                        <td>2022-10-02 10:08:54 +0200</td>
                        <td class="submission-table-original-filename">Perilous Presents.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53964" data-sid="44783">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44783/file/53964">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44783">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Typing Rampage</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="3878442B" id="submission-file-size-53964" data-size="3878442">
                            3.9MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:29 +0200</td>
                        <td>2022-10-02 10:08:54 +0200</td>
                        <td class="submission-table-original-filename">Typing Rampage.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53967" data-sid="44786">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44786/file/53967">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44786">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Save Bob!</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="74960B" id="submission-file-size-53967" data-size="74960">
                            75.0kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:31 +0200</td>
                        <td>2022-10-02 10:08:54 +0200</td>
                        <td class="submission-table-original-filename">Save Bob!.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53971" data-sid="44790">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44790/file/53971">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44790">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Laser Pointer</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="1680025B" id="submission-file-size-53971" data-size="1680025">
                            1.7MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:33 +0200</td>
                        <td>2022-10-02 10:08:54 +0200</td>
                        <td class="submission-table-original-filename">Laser Pointer.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53960" data-sid="44779">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44779/file/53960">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44779">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Super Mouse Adventures</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="390080B" id="submission-file-size-53960" data-size="390080">
                            390.1kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:26 +0200</td>
                        <td>2022-10-02 10:08:53 +0200</td>
                        <td class="submission-table-original-filename">Super Mouse Adventures.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53962" data-sid="44781">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44781/file/53962">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44781">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Sellout</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="10051125B" id="submission-file-size-53962" data-size="10051125">
                            10.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:28 +0200</td>
                        <td>2022-10-02 10:08:53 +0200</td>
                        <td class="submission-table-original-filename">Sellout.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53958" data-sid="44777">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44777/file/53958">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44777">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Hoop60</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="314519B" id="submission-file-size-53958" data-size="314519">
                            314.5kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:24 +0200</td>
                        <td>2022-10-02 10:08:52 +0200</td>
                        <td class="submission-table-original-filename">Hoop60.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="53959" data-sid="44778">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/44778/file/53959">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/44778">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Rob's Cabin Quest</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="1822491B" id="submission-file-size-53959" data-size="1822491">
                            1.8MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-08-24 16:17:25 +0200</td>
                        <td>2022-10-02 10:08:52 +0200</td>
                        <td class="submission-table-original-filename">Rob's Cabin Quest.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="49880" data-sid="40531">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/40531/file/49880">Get</a>
                                
                                    <br><a href="/web/submission/40531/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/40531">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">AOX - Prepare to fail</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="3039732B" id="submission-file-size-49880" data-size="3039732">
                            3.0MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-07-11 14:08:00 +0200</td>
                        <td>2022-07-19 08:05:36 +0200</td>
                        <td class="submission-table-original-filename">AOX - Prepare to fail.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="49631" data-sid="40534">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/40534/file/49631">Get</a>
                                
                                    <br><a href="/web/submission/40534/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/40534">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Tail</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="2867172B" id="submission-file-size-49631" data-size="2867172">
                            2.9MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-07-11 14:52:31 +0200</td>
                        <td>2022-07-18 06:41:29 +0200</td>
                        <td class="submission-table-original-filename">Tail.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="48832" data-sid="40533">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/40533/file/48832">Get</a>
                                
                                    <br><a href="/web/submission/40533/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/40533">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Fallumns!</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="104758B" id="submission-file-size-48832" data-size="104758">
                            104.8kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-07-11 14:36:22 +0200</td>
                        <td>2022-07-14 03:51:19 +0200</td>
                        <td class="submission-table-original-filename">Fallumns!.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="48834" data-sid="40535">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/40535/file/48834">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/40535">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">FlatSpace</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="42749B" id="submission-file-size-48834" data-size="42749">
                            42.7kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-07-11 15:09:31 +0200</td>
                        <td>2022-07-14 03:51:18 +0200</td>
                        <td class="submission-table-original-filename">FlatSpace.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="48826" data-sid="40532">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/40532/file/48826">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/40532">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">InkBall</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="1201303B" id="submission-file-size-48826" data-size="1201303">
                            1.2MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-07-11 14:24:01 +0200</td>
                        <td>2022-07-14 03:51:12 +0200</td>
                        <td class="submission-table-original-filename">InkBall.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="42877" data-sid="36126">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/36126/file/42877">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/36126">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Almost Impossible</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="600939B" id="submission-file-size-42877" data-size="600939">
                            600.9kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-05-22 16:44:19 +0200</td>
                        <td>2022-07-10 04:09:54 +0200</td>
                        <td class="submission-table-original-filename">Almost Impossible.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="43218" data-sid="36425">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/36425/file/43218">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/36425">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">MouseMaze</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Trial</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="298138B" id="submission-file-size-43218" data-size="298138">
                            298.1kB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-05-25 15:21:35 +0200</td>
                        <td>2022-07-09 06:08:50 +0200</td>
                        <td class="submission-table-original-filename">MouseMaze.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="40560" data-sid="34047">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/34047/file/40560">Get</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/34047">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Shine Wars</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Audition</td>
                        <td>irsY</td>
                        <td>BlueMaxima</td>
                        <td class="right" title="2539946B" id="submission-file-size-40560" data-size="2539946">
                            2.5MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-approve">
                            <b>1</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center bgr-verify">
                            <b>1</b>
                        </td>
                        <td>
                            <div class="center-image dot-mark-added" title="Marked as added to Flashpoint."></div>
                        </td>
                        <td>2022-05-08 16:14:45 +0200</td>
                        <td>2022-07-03 13:20:11 +0200</td>
                        <td class="submission-table-original-filename">Shine Wars.7z</td>
                    </tr>
                
                    
                    <tr>
                        <td class="center">
                            
                                <input type="checkbox" class="submission-checkbox" data-fid="39667" data-sid="33290">
                            
                        </td>
                        <td class="center">
                            
                                <a href="/data/submission/33290/file/39667">Get</a>
                                
                                    <br><a href="/web/submission/33290/files">Browse</a>
                                
                            
                        </td>
                        <td class="center">
                            
                                <a href="/web/submission/33290">View</a>
                            
                        </td>
                        <td>
                            
                                <img class="submission-type-icon" src="/static/icons/svg/plus.svg" alt="New Submission">
                            
                        </td>
                        <td class="submission-table-title">Edgar &amp; Ellen - Create a Rare Beast</td>
                        <td>
                        </td>
                        
                        <td>Flash</td>
                        <td>Arcade</td>
                        <td>Audition</td>
                        <td>irsY</td>
                        <td>Rocko Rotten (ItsTheLazytown)</td>
                        <td class="right" title="1112779B" id="submission-file-size-39667" data-size="1112779">
                            1.1MB
                        </td>
                        <td>
                            <div class="center-image dot-approve" title="The bot approves."></div>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td class="center ">
                            <b>0</b>
                        </td>
                        <td>
                            <div class="center-image dot-reject" title="Rejected."></div>
                        </td>
                        <td>2022-04-30 16:32:20 +0200</td>
                        <td>2022-04-30 16:55:53 +0200</td>
                        <td class="submission-table-original-filename">Edgar &amp; Ellen - Create a Rare Beast.7z</td>
                    </tr>
                
                </tbody>
            </table>
        </div>
    </div>
        '''

soup = bs4.BeautifulSoup(text)
titles = []
elements = soup.select(".submission-table-title")

for i in elements:
    title = i.getText()
    titles.append(title)

print(len(titles))

with open("titles.txt", "w", encoding = 'utf-8') as f:
    for i in titles:
        f.write(i + "\n")

with open("titles.txt", "r", encoding = 'utf-8') as f:
    titles= [line.rstrip() for line in f]



con = sqlite3.connect("flashpoint.sqlite")
cur = con.cursor()
ids = []

for title in titles:
    res = cur.execute('SELECT id FROM game WHERE title = ?', (title,))
    try:
        value = res.fetchall()[0][0]
    except:
        continue
    id = value
    ids.append(id)

with open("ids.txt", "w", encoding = 'utf-8') as f:
    for i in ids:
        f.write(i + "\n")

import json

f = open("raw_playlist.json")
old_playlist = json.load(f)
f.close()

with open("ids.txt", "r", encoding = 'utf-8') as f:
    ids= [line.rstrip() for line in f]

new_playlist = old_playlist

games = []
i = 0

for id in ids:
    game = {
        "gameId": id,
        "order" : i,
        "notes": ""
    }
    i = i + 1
    games.append(game)

new_playlist["games"] = games

with open("new_playlist.json", "w") as f:
        json.dump(new_playlist, f, indent=4)
        